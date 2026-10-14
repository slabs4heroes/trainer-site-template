/* Gator Alley — Golden Hour demo: motion + interactions */
(function(){
'use strict';
var doc=document,root=doc.documentElement;
var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
var $=function(s,c){return (c||doc).querySelector(s)};
var $$=function(s,c){return Array.prototype.slice.call((c||doc).querySelectorAll(s))};

/* hero intro */
var hero=$('#hero');
requestAnimationFrame(function(){requestAnimationFrame(function(){hero&&hero.classList.add('go')})});

/* scroll reveal */
var rvs=$$('.rv');
rvs.forEach(function(el){var d=el.getAttribute('data-d');if(d)el.style.transitionDelay=d+'ms'});
if('IntersectionObserver' in window){
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12,rootMargin:'0px 0px -6% 0px'});
  rvs.forEach(function(el){io.observe(el)});
}else rvs.forEach(function(el){el.classList.add('in')});

/* header, progress, parallax, swimmers, method (single rAF loop) */
var header=$('.header'),bar=$('.progress i'),lastY=0,ticking=false;
var para=$$('[data-speed]'),swims=$$('.water'),method=$('#method'),steps=$$('.step'),shots=$$('.shot'),dots=$$('.dots i');
var navLinks=$$('.nav a'),secs=navLinks.map(function(a){return $(a.getAttribute('href'))});
var mobile=function(){return window.innerWidth<=900};
var curStep=-1;
function setStep(i){
  if(i===curStep)return;curStep=i;
  steps.forEach(function(s,k){s.classList.toggle('on',k===i)});
  shots.forEach(function(s,k){s.classList.toggle('on',k===i)});
  dots.forEach(function(s,k){s.classList.toggle('on',k===i)});
}
function frame(){
  ticking=false;
  var y=window.scrollY,vh=window.innerHeight,h=doc.body.scrollHeight-vh;
  header.classList.toggle('shrink',y>40);
  header.classList.toggle('hide',y>lastY+4&&y>500&&!doc.body.classList.contains('menu-open'));
  if(y<lastY-4)header.classList.remove('hide');
  lastY=y;
  bar.style.transform='scaleX('+(h>0?y/h:0)+')';
  if(!reduce){
    para.forEach(function(el){var sp=parseFloat(el.getAttribute('data-speed'))||0;var r=el.getBoundingClientRect();if(r.bottom<-200||r.top>vh+200)return;el.style.translate='0 '+(y*sp)+'px'});
    swims.forEach(function(w){
      var r=w.getBoundingClientRect();if(r.bottom<-300||r.top>vh+300)return;
      var p=Math.min(1,Math.max(0,(vh-r.top)/(vh+120)));
      var sw=w.querySelector('.swimmer');var max=Math.max(40,w.clientWidth-sw.offsetWidth-10);
      w.style.setProperty('--sx',(p*max)+'px');
      sw.style.transform='translateX('+(p*max)+'px)';
    });
  }
  /* pinned method */
  if(method&&!mobile()&&!reduce){
    var mr=method.getBoundingClientRect();var span=mr.height-vh;
    var p2=Math.min(.9999,Math.max(0,-mr.top/span));
    setStep(Math.floor(p2*steps.length));
  }else if(curStep!==-1&&(mobile()||reduce)){curStep=-1;steps.forEach(function(s){s.classList.remove('on')});shots.forEach(function(s){s.classList.add('on')})}
  /* nav highlight */
  var cur=-1;secs.forEach(function(s,i){if(s){var r=s.getBoundingClientRect();if(r.top<vh*.4)cur=i}});
  navLinks.forEach(function(a,i){a.classList.toggle('act',i===cur)});
}
function onScroll(){if(!ticking){ticking=true;requestAnimationFrame(frame)}}
window.addEventListener('scroll',onScroll,{passive:true});window.addEventListener('resize',onScroll);frame();

/* mobile menu */
var mb=$('.menu-btn');
mb.addEventListener('click',function(){var o=doc.body.classList.toggle('menu-open');mb.setAttribute('aria-expanded',o)});
$$('.drawer a').forEach(function(a){a.addEventListener('click',function(){doc.body.classList.remove('menu-open');mb.setAttribute('aria-expanded',false)})});

/* animated counters */
function count(el){
  var end=parseFloat(el.getAttribute('data-count')),dec=parseInt(el.getAttribute('data-dec')||0,10),t0=null,dur=1600;
  if(reduce){el.textContent=end.toFixed(dec);return}
  function step(t){if(!t0)t0=t;var k=Math.min(1,(t-t0)/dur),e=1-Math.pow(1-k,4);el.textContent=(end*e).toFixed(dec);if(k<1)requestAnimationFrame(step)}
  el.textContent=(0).toFixed(dec);requestAnimationFrame(step);
}
if('IntersectionObserver' in window){
  var co=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){count(e.target);co.unobserve(e.target)}})},{threshold:.6});
  $$('[data-count]').forEach(function(el){co.observe(el)});
}

/* 3D tilt + glow on program cards */
$$('.pcard').forEach(function(c){
  if(reduce||!window.matchMedia('(hover:hover)').matches)return;
  c.addEventListener('pointermove',function(e){
    var r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width,y=(e.clientY-r.top)/r.height;
    c.style.setProperty('--ry',((x-.5)*10)+'deg');c.style.setProperty('--rx',((.5-y)*8)+'deg');
    c.style.setProperty('--mx',(x*100)+'%');c.style.setProperty('--my',(y*100)+'%');
  });
  c.addEventListener('pointerleave',function(){c.style.setProperty('--ry','0deg');c.style.setProperty('--rx','0deg')});
});

/* program cards preselect the form */
var sel=$('#program');
$$('[data-program]').forEach(function(a){a.addEventListener('click',function(){
  var v=a.getAttribute('data-program').replace(/&amp;/g,'&');
  if(sel)for(var i=0;i<sel.options.length;i++){if(sel.options[i].text===v){sel.selectedIndex=i;break}}
})});

/* fireflies */
var mouse={x:-9999,y:-9999,on:false};
window.addEventListener('pointermove',function(e){mouse.cx=e.clientX;mouse.cy=e.clientY;mouse.on=true},{passive:true});
function flies(cv){
  var ctx=cv.getContext('2d'),W=0,H=0,ps=[],dpr=Math.min(2,window.devicePixelRatio||1),vis=false,raf=0;
  function size(){var r=cv.parentNode.getBoundingClientRect();W=r.width;H=r.height;cv.width=W*dpr;cv.height=H*dpr;ctx.setTransform(dpr,0,0,dpr,0,0);
    var n=Math.round(Math.min(46,Math.max(16,W*H/38000)));while(ps.length<n)ps.push({x:Math.random()*W,y:Math.random()*H,vx:(Math.random()-.5)*.3,vy:(Math.random()-.5)*.3,r:Math.random()*1.8+1,ph:Math.random()*6.28,sp:.01+Math.random()*.02});ps.length=n}
  function draw(){
    raf=0;if(!vis)return;
    ctx.clearRect(0,0,W,H);
    var rect=cv.getBoundingClientRect(),mx=mouse.on?mouse.cx-rect.left:-9999,my=mouse.on?mouse.cy-rect.top:-9999;
    ps.forEach(function(p){
      p.ph+=p.sp;p.vx+=(Math.random()-.5)*.03;p.vy+=(Math.random()-.5)*.03;
      var dx=mx-p.x,dy=my-p.y,d=Math.sqrt(dx*dx+dy*dy);
      if(d<220){p.vx+=dx/d*.012;p.vy+=dy/d*.012}
      p.vx*=.985;p.vy*=.985;p.x+=p.vx;p.y+=p.vy;
      if(p.x<-10)p.x=W+10;if(p.x>W+10)p.x=-10;if(p.y<-10)p.y=H+10;if(p.y>H+10)p.y=-10;
      var a=.35+.65*Math.abs(Math.sin(p.ph)),g=ctx.createRadialGradient(p.x,p.y,0,p.x,p.y,p.r*9);
      g.addColorStop(0,'rgba(217,255,99,'+a+')');g.addColorStop(.25,'rgba(217,255,99,'+(a*.35)+')');g.addColorStop(1,'rgba(217,255,99,0)');
      ctx.fillStyle=g;ctx.beginPath();ctx.arc(p.x,p.y,p.r*9,0,6.283);ctx.fill();
      ctx.fillStyle='rgba(255,255,220,'+a+')';ctx.beginPath();ctx.arc(p.x,p.y,p.r*.8,0,6.283);ctx.fill();
    });
    raf=requestAnimationFrame(draw);
  }
  size();window.addEventListener('resize',size);
  if(reduce){vis=true;draw();return}
  new IntersectionObserver(function(es){vis=es[0].isIntersecting;if(vis&&!raf)raf=requestAnimationFrame(draw)},{rootMargin:'100px'}).observe(cv);
}
$$('.flies').forEach(flies);

/* lightbox (uncropped, full-size) */
var lb=$('#lb'),lbImg=lb.querySelector('img'),lbCap=lb.querySelector('figcaption'),items=$$('.pol:not(.dup)'),idx=0;
function show(i){
  idx=(i+items.length)%items.length;var b=items[idx],im=b.querySelector('img');
  lbImg.src=im.currentSrc||im.src;lbImg.alt=im.alt;lbCap.textContent=b.getAttribute('data-cap')||'';
}
function openLb(b){var i=items.indexOf(b);if(i<0){var s=b.querySelector('img').getAttribute('src');i=items.findIndex(function(x){return x.querySelector('img').getAttribute('src')===s});if(i<0)i=0}
  show(i);if(!lb.open)lb.showModal()}
$$('.pol').forEach(function(b){b.addEventListener('click',function(){openLb(b)})});
lb.querySelector('.lb-x').addEventListener('click',function(){lb.close()});
lb.querySelector('.prev').addEventListener('click',function(){show(idx-1)});
lb.querySelector('.next').addEventListener('click',function(){show(idx+1)});
lb.addEventListener('click',function(e){if(e.target===lb)lb.close()});
lb.addEventListener('keydown',function(e){if(e.key==='ArrowLeft')show(idx-1);if(e.key==='ArrowRight')show(idx+1)});

/* forms (DEMO: nothing is sent anywhere) */
$$('[data-form]').forEach(function(f){
  f.addEventListener('submit',function(e){
    e.preventDefault();var msg=f.querySelector('.form-msg'),ok=true;
    $$('input[required]',f).forEach(function(i){if(!i.value.trim()||(i.type==='email'&&i.value.indexOf('@')<1))ok=false});
    if(!ok){msg.style.color='#c0361b';msg.textContent='Please fill in your name, phone and a valid email.';return}
    msg.style.color='';msg.textContent='Demo preview: this form is not connected yet. On the live site this goes straight to Jacob.';
    f.reset();
  });
});
})();

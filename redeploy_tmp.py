import asyncio, json
from deploy_vercel import deploy

async def main():
    resp = await deploy("/work/temp/lmk9_template_demo/site_out_hosted", "trainer-site-template-lmk9", prod=False, inline=True)
    print(json.dumps(resp, indent=2)[:3000])

asyncio.run(main())

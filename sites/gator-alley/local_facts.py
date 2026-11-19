# Sourced local facts for each service-area town.
# Every statement here was read on the official page linked by its source key (checked 2026-11-19).
# If a fact cannot be tied to an official page it does not belong in this file.

SRC = {
    "mt_license": ("Manatee County: license a pet", "https://www.mymanatee.org/departments/public_safety/animal_services/license_a_pet/"),
    "mt_pets": ("Manatee County: parks and preserves pet policy", "https://www.mymanatee.org/departments/parks___natural_resources/parks__preserves___beaches/pet_policies/"),
    "mt_dogparks": ("Manatee County: dog parks", "https://manatee.hosted.civiclive.com/dogparks"),
    "mt_preserve_faq": ("Manatee County 311: dogs in county preserves", "https://manateecountyfl.qscend.com/311/knowledgebase/article/571"),
    "mt_nr": ("Manatee County: natural resources and preserves", "https://www.mymanatee.org/departments/natural_resources"),
    "fsp_lkm": ("Florida State Parks: Lake Manatee State Park", "https://www.floridastateparks.org/parks-and-trails/lake-manatee-state-park/experiences-amenities-0"),
    "fsp_lkm_map": ("Florida State Parks: Lake Manatee brochure", "https://www.floridastateparks.org/sites/default/files/media/file/lkm-brochure_1.pdf"),
    "fsp_rules": ("Florida State Parks: park rules", "https://www.floridastateparks.org/florida-state-park-rules"),
    "fsp_gamble": ("Florida State Parks: Gamble Plantation brochure", "https://www.floridastateparks.org/sites/default/files/media/file/gph-brochure_0.pdf"),
    "lwr_rules": ("Lakewood Ranch Stewardship District: amenity rules", "https://lakewoodranchstewardship.com/wp-content/uploads/2021/05/amenity_rules__rates-_lwrsd-5.pdf"),
    "hc_ord": ("Hillsborough County: commonly cited animal ordinances", "https://hcfl.gov/residents/animals-and-pets/pet-related-ordinances-and-citations/commonly-cited-animal-ordinances"),
    "hc_dogparks": ("Hillsborough County: find a dog park", "https://hcfl.gov/residents/animals-and-pets/pet-ownership/find-a-dog-park"),
    "hc_rules": ("Hillsborough County: conservation park rules", "https://hcfl.gov/residents/parks-and-leisure/outdoor-recreation/rules-and-expectations"),
    "hc_neighbor": ("Hillsborough County: be a good neighbor to nature", "https://hcfl.gov/residents/parks-and-leisure/conservation-lands/be-a-good-neighbor-to-nature"),
    "hc_heat": ("Hillsborough County: extreme heat information", "https://hcfl.gov/residents/stay-safe/extreme-heat-information"),
    "hc_simmons": ("Hillsborough County: E.G. Simmons Conservation Park brochure", "https://assets.contentstack.io/v3/assets/blteea73b27b731f985/blt38a77d213f407405/EG%20Simmons%20Brochure.pdf"),
    "hc_simmons_hours": ("Hillsborough County: E.G. Simmons hours", "https://assets.contentstack.io/v3/assets/blteea73b27b731f985/blt5c5200eff5910d11/EG%20Simmons%20Campground%20Brochure.pdf"),
    "hc_lmrc": ("Hillsborough County: Little Manatee River Corridor Nature Preserve", "https://hcfl.gov/locations/little-manatee-river-corridor-nature-preserve"),
    "hc_bellcreek": ("Hillsborough County: Bell Creek Nature Preserve", "https://hcfl.gov/locations/bell-creek-preserve"),
    "tpa_rules": ("City of Tampa: dog park rules", "https://www.tampa.gov/parks-and-recreation/parks-and-facilities/dog-parks/dog-park-rules-and-regulations"),
    "tpa_parks": ("City of Tampa: dog parks and leash-free areas", "https://www.tampa.gov/parks-and-recreation/parks-and-natural-areas/dog-parks"),
    "stp_pets": ("City of St. Petersburg: pet ownership guide", "https://www.stpete.org/residents/good_neighbor_guides/pet_ownership.php"),
    "stp_parks": ("St. Petersburg Parks & Recreation: dog parks", "https://stpeteparksrec.org/dogparks"),
    "sar_tag": ("Sarasota County Sheriff: animal services registration", "https://sarasotasheriff.org/programs_and_amp_services/animal_services/make_payments_online.php"),
    "sar_fees": ("Sarasota County Sheriff: ordinance fees and fines", "https://sarasotasheriff.org/programs_and_amp_services/animal_services/county_ordinance_fees.php"),
    "sar_parks": ("Sarasota County Parks: dog parks and dog-friendly parks", "https://www.sarasotacountyparks.com/parks-and-facilities/discover-a-park/type-of-park/dog-parks-and-dog-friendly-parks"),
    "ven_brohard": ("City of Venice: Brohard Paw Park", "https://venicegov.com/things-to-do/parks-and-beaches/brohard-paw-park"),
    "np_canine": ("City of North Port: Canine Club Dog Park", "https://northportfl.gov/Community-Recreation/Parks-Facilities/Parks/Park-Pages/Canine-Club-Dog-Park"),
    "fl_heat": ("Florida Division of Emergency Management: extreme heat", "https://www.floridadisaster.org/weather/hazards/heat-wave/"),
    "nws_heat": ("National Weather Service Tampa Bay: heat tools", "https://weather.gov/tbw/heat"),
}

# each town: heading, intro (2 paragraphs), rules [(text, [src])], places [(name, detail, [src])],
# safety (text, [src]), faq (question, answer, [src])
TOWNS = {
    "parrish": dict(
        headline="Parrish dogs live under Manatee County rules",
        intro=[
            "Gator Alley Dog Training is at 10328 Charlotte Dr in Parrish, so for Parrish owners the training home is right in town. What a trainer can build in a few weeks still has to work inside the rules your dog lives under every day, and in Parrish those are Manatee County's.",
            "Below are the county and state rules that matter most when you walk, license and exercise a dog in the Parrish area, each tied to the official page it came from.",
        ],
        rules=[
            ("Manatee County asks owners of dogs, cats and ferrets to keep a yearly rabies vaccination and a county license, and it will not sell a license without proof of a current rabies shot.", ["mt_license"]),
            ("The county lists fines of $200, $350 and $500 for a first, second and third failure to get a license tag, and says non-registration can reach $1,000.", ["mt_license"]),
            ("In county parks and preserves a dog has to be on a leash the whole time.", ["mt_pets"]),
        ],
        places=[
            ("Ola Mae Sims Park Happy Paws Dog Park", "11800 Erie Road, Parrish. The county lists separate large-dog and small-dog areas.", ["mt_dogparks"]),
            ("Rye Preserve", "905 Rye Wilderness Trail. County preserves welcome leashed dogs, with four exceptions (Leffis Key, Moody Branch, Neal and Perico).", ["mt_preserve_faq"]),
            ("Lake Manatee State Park", "On State Road 64 east of I-75. Pets are allowed on a 6-foot hand-held leash and may not be left unattended.", ["fsp_lkm", "fsp_lkm_map"]),
        ],
        safety=("Manatee County's pet policy page carries a “Keep it Cool” reminder for hot days, and notes that not every trail has shade. Pack water for your dog before a summer walk.", ["mt_pets"]),
        faq=("What does my Parrish dog legally need before it goes to a dog park?",
             "The county's dog park rules ask for a current license tag and a current rabies vaccination, a leash on the way in and out, and an owner who stays in view with a leash in hand. Dogs in heat and aggressive dogs are not allowed to stay.", ["mt_dogparks"]),
    ),
    "bradenton": dict(
        headline="Bradenton: licensing, dog parks and where dogs cannot go",
        intro=[
            "Bradenton is in Manatee County, which lists several fenced dog parks and also names places where dogs are not allowed. Knowing the boundaries helps, because the places you practice are the places your dog will be tested.",
            "These notes come straight from Manatee County pages, so you can check any of them yourself before heading out.",
        ],
        rules=[
            ("A Manatee County pet license costs $20 at Animal Welfare, and tags can also be bought or looked up through PetData.", ["mt_license"]),
            ("Dogs are not allowed at county beaches, and that includes the sidewalks, paths, trails and parking areas next to them. They are also off-limits at athletic fields and anywhere posted “no dogs allowed.”", ["mt_pets"]),
            ("County dog parks ban choke collars and require dogs to be leashed on entry and exit and off leash inside the fence.", ["mt_dogparks"]),
        ],
        places=[
            ("Creekwood Park Paw Patch Dog Park", "7025 44th Avenue East, Bradenton. Large-dog and small-dog areas.", ["mt_dogparks"]),
            ("Laurie Crawford Dog Park at G.T. Bray Park", "51st Street, Bradenton. The county lists large-dog and small-dog areas here too.", ["mt_dogparks"]),
            ("Robinson Preserve", "Not on the county's no-dogs list, so leashed dogs are allowed on its trails. The beach rule above still applies, so watch for posted signs near the water.", ["mt_preserves_list"]),
        ],
        safety=("Florida's emergency management agency warns that a parked car can reach 135 degrees in under ten minutes. A short errand is not a short wait for a dog, so the dog stays home or comes with you.", ["fl_heat"]),
        faq=("Can I bring my dog to a Bradenton-area county beach?",
             "No. Manatee County's pet policy says dogs are not allowed at county beaches, including adjacent sidewalks, paths, trails and parking areas. The county's dog parks and leashed preserve trails are the places to go instead.", ["mt_pets"]),
    ),
    "sarasota": dict(
        headline="Sarasota County tags, fines and paw parks",
        intro=[
            "Sarasota dog owners answer to the Sarasota County Sheriff's Office for animal services, and the county runs a network of paw parks. If you are choosing between Gator Alley's board-and-train in Parrish and live Zoom coaching, this is the local picture your dog has to fit into either way.",
            "Everything below links to the official page it was read from.",
        ],
        rules=[
            ("The Sheriff's Animal Services page says every dog and cat four months or older needs a registration tag.", ["sar_tag"]),
            ("The county's fee schedule lists fines of $50, $100 and $200 for failure to license under Section 14-38(d).", ["sar_fees"]),
            ("At Sarasota County's dog-friendly parks, a dog stays on a hand-held leash no longer than 6 feet at all times, and dogs are kept out of playgrounds and athletic fields.", ["sar_parks"]),
        ],
        places=[
            ("17th Street Park, Bay Street, Lakeview Park and Woodmere Park", "County-managed off-leash dog parks named on Sarasota County Parks' dog park page.", ["sar_parks"]),
            ("South Brohard Paw Park", "The county lists an off-leash beach area here.", ["sar_parks"]),
        ],
        safety=("The National Weather Service Tampa Bay office publishes heat-index maps for Southwest Florida. Check the day's reading before a midday walk.", ["nws_heat"]),
        faq=("Who do I call about a dog tag or animal complaint in Sarasota County?",
             "Sarasota County Sheriff's Animal Services handles registration tags and animal service calls. Its page lists (941) 861-9500 and says tags are required for dogs and cats four months or older.", ["sar_tag"]),
    ),
    "lakewood-ranch": dict(
        headline="Lakewood Ranch sits on a county line; its dog park has its own rules",
        intro=[
            "Lakewood Ranch spreads across Manatee and Sarasota counties, so which county license applies depends on your address. Your neighbors may follow different paperwork than you do.",
            "The community's best-known dog park is run by the Lakewood Ranch Stewardship District rather than a county, and it has its own sign-up. Here is what the district's published rules say.",
        ],
        rules=[
            ("If your address is in Manatee County, the county requires a yearly rabies vaccination and a license.", ["mt_license"]),
            ("If your address is in Sarasota County, the Sheriff's Animal Services requires a registration tag for dogs four months or older.", ["sar_tag"]),
            ("The Stewardship District's dog park is for registered dogs only. Dogs must wear current county tags and have a current rabies vaccination.", ["lwr_rules"]),
        ],
        places=[
            ("Bob Gardner Park dog park", "Run by the Lakewood Ranch Stewardship District. Open dawn to dusk, not staffed, leash on entering and exiting, and the district recommends the small-dog area for small, fragile or elderly dogs. Its rules document is dated 2018 and lists annual fees, so confirm current registration costs with the district before you go.", ["lwr_rules"]),
        ],
        safety=("Florida's emergency management agency lists never leaving children or pets in a parked car as its first heat rule. Plan Lakewood Ranch errands so the dog is never waiting in the car.", ["fl_heat"]),
        faq=("Do I need to register my dog to use the Lakewood Ranch dog park?",
             "Yes. The Stewardship District's rules say only registered dogs and their owners may use the park, and registration goes through a form sent to the district's parks email. Confirm the current form and fees with the district, since the published document is from 2018.", ["lwr_rules"]),
    ),
    "palmetto": dict(
        headline="Palmetto: a county dog park and a preserve on 17th Street West",
        intro=[
            "Jacob was born and raised in Palmetto. Palmetto's official dog options sit with Manatee County, which publishes both its dog park rules and its preserve policies online.",
            "Here is what the county says, with a link to each page.",
        ],
        rules=[
            ("Manatee County publishes two numbers on its dog park page: Animal Services at (941) 747-5933 and the Sheriff's Office at (941) 747-3011.", ["mt_dogparks"]),
            ("All of the county's preserves have marked trails, and the county asks people and dogs to stay on them because off-trail use damages habitat.", ["mt_pets"]),
            ("Dogs are allowed in county preserves on a leash, except Leffis Key, Moody Branch, Neal and Perico.", ["mt_preserve_faq"]),
        ],
        places=[
            ("Blackstone Park dog park", "2112 14th Avenue West, Palmetto. The county lists large-dog and small-dog areas.", ["mt_dogparks"]),
            ("Emerson Point Preserve", "5801 17th Street West, Palmetto. The county lists it as open daily from sunrise to sunset. The preserve lists a beach, and the county does not allow dogs at county beaches, so follow posted signs.", ["mt_nr", "mt_pets"]),
        ],
        safety=("The National Weather Service Tampa Bay office posts heat tools for West Central Florida. Check the heat index before a midday walk.", ["nws_heat"]),
        faq=("Where can my Palmetto dog run off leash?",
             "Blackstone Park's dog park is the county's listed option in Palmetto. Inside the fence dogs are off leash, and they must be leashed entering and leaving. The county asks for a current license tag and rabies vaccination.", ["mt_dogparks"]),
    ),
    "ellenton": dict(
        headline="Ellenton: county rules plus a state park with limits on pets",
        intro=[
            "Ellenton owners share Manatee County's licensing rules and its dog parks in nearby Palmetto and Bradenton. The local landmark, Gamble Plantation Historic State Park, is a state park, which means state pet rules apply there.",
            "The notes below point to the official pages so you can confirm anything before a visit.",
        ],
        rules=[
            ("Manatee County says pets must be licensed, and a license requires proof of a current rabies vaccination.", ["mt_license"]),
            ("Florida State Parks say pets are allowed only in designated areas, on a hand-held leash no longer than six feet.", ["fsp_rules"]),
        ],
        places=[
            ("Gamble Plantation Historic State Park", "3708 Patten Avenue, Ellenton, phone (941) 723-4536. Because state parks only allow pets in designated areas, call ahead to ask where your dog can go.", ["fsp_gamble", "fsp_rules"]),
            ("County dog parks in nearby Palmetto and Bradenton", "Blackstone Park in Palmetto and Creekwood Park or G.T. Bray Park in Bradenton are the nearest on Manatee County's list.", ["mt_dogparks"]),
        ],
        safety=("Florida's emergency management agency says a parked car can reach 135 degrees in under ten minutes. On an Ellenton errand run, leave the dog at home.", ["fl_heat"]),
        faq=("Can I bring my dog to Gamble Plantation Historic State Park in Ellenton?",
             "Florida State Parks allow pets only in designated areas, on a hand-held leash of six feet or less. Call the park at (941) 723-4536 to confirm where dogs are permitted before you go.", ["fsp_rules", "fsp_gamble"]),
    ),
    "ruskin": dict(
        headline="Ruskin: a conservation park with a strict leash rule",
        intro=[
            "Ruskin is in Hillsborough County, which publishes its animal ordinances online. For a dog in training, the everyday rule that matters most is the leash.",
            "These are the county's own words on leashes and tethering, followed by one of Ruskin's best-known public spaces.",
        ],
        rules=[
            ("Hillsborough County requires a leash no longer than six feet and says the dog must stay under the owner's immediate and continuous physical control (Sec. 38-26). Fines run from $100 up to $500 for repeat violations.", ["hc_ord"]),
            ("The county bans unattended tethering. Tethering is allowed only if the owner stays outside in sight of the dog (Sec. 6-33), with fines starting at $370.", ["hc_ord"]),
        ],
        places=[
            ("E.G. Simmons Conservation Park", "2401 19th Ave. NW, Ruskin. Pets must be on a leash of six feet or shorter that is non-retractable, and pets are not allowed inside facilities. Hours listed for spring and summer are 8 a.m. to 7 p.m.; fall and winter are 8 a.m. to 6 p.m.", ["hc_simmons", "hc_simmons_hours"]),
        ],
        safety=("Hillsborough County's extreme heat page says cars heat up fast even with a window cracked, so pets should never be left inside one.", ["hc_heat"]),
        faq=("Can I use a retractable leash at E.G. Simmons Conservation Park?",
             "Hillsborough County's brochure for the park asks for a non-retractable leash of six feet or shorter and says pets must be in your control at all times. A fixed-length leash is also a better training tool.", ["hc_simmons"]),
    ),
    "apollo-beach": dict(
        headline="Apollo Beach: registration rules and a county dog park",
        intro=[
            "Apollo Beach dog owners follow Hillsborough County's animal ordinances, and the county runs its own dog park in town. The rules on registration and rabies vaccination are the ones new owners most often miss.",
            "Here are the specifics, each linked to the county page it came from.",
        ],
        rules=[
            ("Hillsborough County requires all dogs, cats and ferrets four months or older to be registered (Sec. 6-22), renewed yearly or every three years depending on the rabies vaccine type.", ["hc_ord"]),
            ("The same county rules require a rabies vaccination for animals four months or older (Sec. 6-21). Fines for these violations start at $100.", ["hc_ord"]),
        ],
        places=[
            ("Apollo Beach Dog Park", "664 Golf and Sea Blvd., Apollo Beach. The county asks you to take the leash off in the transition area before entering, bans food for dogs and people, and asks you to leave toys, including small splash pools, at home. Scoop bags are provided.", ["hc_dogparks"]),
        ],
        safety=("Hillsborough County's extreme heat page also links to heat.gov's pet safety guidance. On a hot day, shorten the walk and carry water.", ["hc_heat"]),
        faq=("What are the rules at the Apollo Beach Dog Park?",
             "Hillsborough County's dog park rules ask owners to leave food and toys at home, fill any holes their dog digs, and keep anyone under 16 with an adult. Dogs declared dangerous or aggressive are not allowed, and the dog should stay leashed everywhere outside the fence.", ["hc_dogparks"]),
    ),
    "sun-city-center": dict(
        headline="Sun City Center: leash law, preserve trails and what to carry",
        intro=[
            "Sun City Center is in southern Hillsborough County, where the county manages river-corridor nature preserves. Walking a dog on those trails comes with a short list of county rules that apply to everyone.",
            "The notes below are taken from county pages on preserves and parks.",
        ],
        rules=[
            ("Hillsborough County states that dogs must be leashed while inside its nature preserves and parks.", ["hc_neighbor"]),
            ("On conservation parks and preserves, pets must be restrained on a hand-held leash and their waste scooped and put in the trash.", ["hc_rules"]),
        ],
        places=[
            ("Little Manatee River Corridor Nature Preserve", "In southern Hillsborough County. The 579 trailhead access point has a 1.5-mile short loop and a 3.5-mile long loop, and another trailhead is at 2510 Leonard Lee Road in Wimauma.", ["hc_lmrc"]),
        ],
        safety=("The county's hiking safety guidance for this preserve starts with bringing plenty of water. Dogs need it too, so carry a bowl as well as a bottle.", ["hc_lmrc"]),
        faq=("Do Hillsborough County preserves allow dogs?",
             "Yes, on a leash. The county says dogs must be leashed in its nature preserves and parks, and its conservation park rules require a hand-held leash and picking up waste.", ["hc_neighbor", "hc_rules"]),
    ),
    "riverview": dict(
        headline="Riverview: a county preserve off McMullen Road",
        intro=[
            "Riverview is in Hillsborough County and has a county nature preserve. For dogs, the preserve and the county's tethering rules are the two things worth knowing first.",
            "Both come from official Hillsborough County pages linked below.",
        ],
        rules=[
            ("Hillsborough County's tethering rule (Sec. 6-33) bans unattended tethering. If a dog is tethered, the owner must stay outside with it and keep it in sight.", ["hc_ord"]),
            ("The county's park rules require pets on conservation lands to be restrained on a hand-held leash, with waste scooped and thrown out.", ["hc_rules"]),
        ],
        places=[
            ("Bell Creek Nature Preserve", "A 477-acre preserve east of McMullen Road and south of Boyette Road in Riverview, with an administrative office where park passes can be bought.", ["hc_bellcreek"]),
        ],
        safety=("Hillsborough County's extreme heat page asks everyone to keep pets out of parked cars, since a cracked window does not keep a car cool.", ["hc_heat"]),
        faq=("Is it legal to leave my dog tied up outside in Riverview?",
             "Only if you stay outside with the dog and keep it in sight. Hillsborough County bans unattended tethering and sets minimum fines of $370 for violations.", ["hc_ord"]),
    ),
    "brandon": dict(
        headline="Brandon: Saladino Dog Park and the county's park etiquette",
        intro=[
            "Brandon has one of Hillsborough County's official dog parks, Saladino Dog Park, and the county posts clear etiquette for using it. Following that etiquette is also good practice for a dog that is learning to ignore other dogs.",
            "The details below are from the county's dog park page.",
        ],
        rules=[
            ("Dogs declared dangerous or aggressive are not allowed in county dog parks, and dogs that show aggression can be removed at staff request.", ["hc_dogparks"]),
            ("The county asks owners to get permission before approaching someone else's dog and to leave if their own dog is provoking others.", ["hc_dogparks"]),
            ("Only one dog should be in the transition entrance at a time.", ["hc_dogparks"]),
        ],
        places=[
            ("Saladino Dog Park", "1705 Bryan Rd., Brandon. The county posts the rules at each park as well as online.", ["hc_dogparks"]),
        ],
        safety=("Hillsborough County's extreme heat page reminds owners that a car can become dangerous quickly even with the window open.", ["hc_heat"]),
        faq=("What should I know before taking my dog to Saladino Dog Park in Brandon?",
             "Take the leash off in the transition area, leave toys and food at home, pick up waste and fill any holes. Dogs must be leashed everywhere outside the fenced area, which the county treats as part of its leash law.", ["hc_dogparks"]),
    ),
    "tampa": dict(
        headline="Tampa: 18 listed dog parks, with city rules that apply to all of them",
        intro=[
            "The City of Tampa lists 18 dog parks and leash-free areas, and publishes one set of rules for its dog parks.",
            "That makes Tampa a good place to practice calm greetings and recall, as long as the rules are followed.",
        ],
        rules=[
            ("Tampa's dog park rules (Ordinance 2001-59) require dogs to be licensed, wear ID tags, and be at least four months old.", ["tpa_rules"]),
            ("Off-leash dogs are limited to two per person, rawhide and food are not allowed, and dogs must be leashed before entering and leaving.", ["tpa_rules"]),
            ("Outside the designated area dogs stay leashed, including the parking lot, and dogs are not allowed on city beaches except a designated dog beach.", ["tpa_parks"]),
        ],
        places=[
            ("Davis Islands Dog Park & Dog Beach", "1002 Severn St., Tampa.", ["tpa_parks"]),
            ("Picnic Island Dog Beach", "7409 Picnic Island Blvd., Tampa.", ["tpa_parks"]),
            ("Curtis Hixon Waterfront Park dog park", "600 N Ashley Drive. The city lists a maintenance closing from 2 to 4 p.m. on Tuesdays and Fridays.", ["tpa_parks"]),
        ],
        safety=("The city's dog park page reminds visitors that they and their pets may meet wildlife, and asks you to stay aware of your surroundings.", ["tpa_parks"]),
        faq=("How many dogs can I take off leash at a Tampa dog park?",
             "The city's rules limit off-leash dogs to two per person inside the park, and dogs must be leashed entering and leaving. Dogs must also be licensed and at least four months old.", ["tpa_rules"]),
    ),
    "st-petersburg": dict(
        headline="St. Petersburg: six city dog parks and a 6-foot leash rule",
        intro=[
            "St. Petersburg is in Pinellas County, across Tampa Bay from Manatee County, so owners here often start with a live Zoom session. The city's public rules on leashes and dog parks are short and clear.",
            "Both come from the city's own pages, linked below.",
        ],
        rules=[
            ("The city's pet ownership guide says to keep dogs on a leash no longer than 6 feet in areas open to the public, including city parks (adapted from City Ordinance Sec. 4-55).", ["stp_pets"]),
            ("Dogs may be off leash only in fenced, designated dog parks.", ["stp_pets"]),
        ],
        places=[
            ("Coquina Key", "3595 Locust St. SE.", ["stp_parks"]),
            ("Crescent Lake", "1320 5th St. N.", ["stp_parks"]),
            ("Kenwood Park", "401 20th St. N.", ["stp_parks"]),
            ("Lake Vista Park", "1401 62nd Ave. S.", ["stp_parks"]),
            ("North Shore", "901 North Shore Dr. NE.", ["stp_parks"]),
            ("Walter Fuller", "7901 30th Ave. N. Parks are open from 30 minutes before sunrise to 30 minutes after sunset and close briefly for weekly maintenance.", ["stp_parks"]),
        ],
        safety=("Florida's emergency management agency says a parked car can reach 135 degrees in under ten minutes. Keep dogs out of the car on bay-side errands.", ["fl_heat"]),
        faq=("Where can a St. Petersburg dog run off leash?",
             "Only in the city's fenced dog parks: Coquina Key, Crescent Lake, Kenwood, Lake Vista, North Shore and Walter Fuller. Everywhere else in public the leash can be no longer than six feet.", ["stp_pets", "stp_parks"]),
    ),
    "venice": dict(
        headline="Venice: the only Sarasota County beach where dogs are allowed",
        intro=[
            "Venice owners have an unusual local perk. The city's Brohard Paw Park leads to what the city calls the only beach area in Sarasota County where dogs are allowed.",
            "That perk has rules, and so does the rest of the county. Here is what the official pages say.",
        ],
        rules=[
            ("Brohard Paw Park is open daily from 7 a.m. to dusk, and dogs can use the beach only up to the posted sign that marks where the dog beach ends.", ["ven_brohard"]),
            ("Sarasota County Sheriff's Animal Services requires a registration tag for dogs four months or older.", ["sar_tag"]),
        ],
        places=[
            ("Brohard Paw Park", "1850 Harbor Drive S., Venice. A fenced dog play yard, plus access to the dog beach. The city notes the park is maintained by the county, and waste bags are provided.", ["ven_brohard"]),
            ("Woodmere Park", "Listed by Sarasota County Parks among its county-managed off-leash dog parks.", ["sar_parks"]),
        ],
        safety=("Florida's emergency management agency lists heat rules for pets as well as people. At the beach, shade and fresh water matter as much as the swim.", ["fl_heat"]),
        faq=("Can I take my dog on a beach in Venice?",
             "Only at Brohard Paw Park's dog beach, and only up to the posted sign. The city's page says it is the only beach area in Sarasota County where dogs are allowed.", ["ven_brohard"]),
    ),
    "north-port": dict(
        headline="North Port: city code that follows Sarasota County's animal rules",
        intro=[
            "North Port's City Code Section 10-31 adopts the Sarasota County Animal Control Ordinance, so the county's animal rules apply to North Port dogs.",
            "The city's Canine Club Dog Park spells those rules out, so it doubles as a plain-language guide.",
        ],
        rules=[
            ("The city's Canine Club page says pet owners must follow the Sarasota County Animal Control Ordinance, which North Port adopts under City Code Section 10-31.", ["np_canine"]),
            ("Dogs at the park must be vaccinated and wear current tags, and each handler may bring no more than three dogs.", ["np_canine"]),
            ("Leashes can be no longer than six feet, and dogs must be leashed entering and leaving, including in the parking lot.", ["np_canine"]),
        ],
        places=[
            ("Canine Club Dog Park", "6700 Appomattox Drive, North Port. A fully fenced 1.5-acre park with separate large-dog and small-dog areas (the small-dog side has a 20-pound limit). It is open sunrise to sunset and closes all day Wednesday for maintenance.", ["np_canine"]),
        ],
        safety=("The park lists shade structures and canine cooling stations. Even so, carry your own water, since Florida heat builds quickly.", ["np_canine", "fl_heat"]),
        faq=("Which animal rules apply to dogs in North Port?",
             "The Sarasota County Animal Control Ordinance, which the city adopts under City Code Section 10-31. At the Canine Club Dog Park that includes vaccinations, current tags and a six-foot leash limit.", ["np_canine"]),
    ),
}

SRC["mt_preserves_list"] = ("Manatee County: preserves list", "https://manatee.hosted.civiclive.com/departments/natural_resources/preserves")

LEDES = {
    "parrish": "Gator Alley Dog Training is based in Parrish. Personally led board-and-train programs in a real home, built around the way your dog actually lives.",
    "bradenton": "Board-and-train programs for Bradenton dog owners, personally led by Jacob in a real home environment, not a kennel.",
    "sarasota": "Sarasota owners can train with Jacob through personally led board-and-train programs, plus live virtual coaching over Zoom.",
    "lakewood-ranch": "Board-and-train programs for Lakewood Ranch families, personally led by Jacob in Parrish.",
    "palmetto": "Jacob was born and raised in Palmetto and trains in Parrish. Personally led board-and-train programs for puppies and adult dogs.",
    "ellenton": "Ellenton owners can work with Jacob through board-and-train programs at his home in Parrish, led personally by Jacob.",
    "ruskin": "Ruskin owners can send their dog to Jacob's home in Parrish for a personally led board-and-train, or start with live Zoom coaching.",
    "apollo-beach": "Apollo Beach owners can work with Jacob through personally led board-and-train in Parrish, with Zoom coaching as another way in.",
    "sun-city-center": "Sun City Center owners get a personally led trainer who treats each dog as an individual, plus live Zoom coaching for those who prefer to learn at home.",
    "riverview": "Riverview owners can send their dog to Jacob's home in Parrish for a personally led board-and-train, or begin with a live Zoom session from the living room.",
    "brandon": "Brandon families can work with Jacob in person through board-and-train in Parrish, or start closer to home with a live Zoom coaching session.",
    "tampa": "Tampa owners can book a free consultation with Jacob to discuss personally led board-and-train in Parrish, or train from home over live Zoom sessions.",
    "st-petersburg": "St. Petersburg owners can work with Jacob through live Zoom coaching, or arrange board-and-train at his home in Parrish.",
    "venice": "Venice owners can train with Jacob through board-and-train programs in Parrish or live virtual coaching over Zoom.",
    "north-port": "North Port owners can train with Jacob through board-and-train programs in Parrish or live virtual coaching over Zoom.",
}
for _k, _v in LEDES.items():
    TOWNS[_k]["lede"] = _v

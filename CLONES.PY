import time
import os
import sys
import itertools

# Updated ASCII banner for "EXOTIC" (larger and bolder)
BANNER = r"""
EXOTIC-CLONES.CA
"""

# Strain data from PHP, converted to Python list of dictionaries
CLONES = [
    {"name": "Papaya", "price": 99.99, "description": "Carefully selected from over 100 seeds sourced from Nirvana Seed Bank, our Papaya phenotype is a standout gem. This cultivar delivers a rich, tropical papaya aroma layered with sweet, dank undertones and an unforgettable smooth finish. Beyond its exotic flavor profile, this pheno is a dream for solventless extraction artists yielding over 4% in hash rosin returns. Whether you’re a connoisseur grower or a rosin enthusiast, this Papaya cut was handpicked to impress on every level."},
    {"name": "Zkittlez aka z", "price": 199.99, "description": "The original Z, also known as Zkittlez, is a one-of-a-kind cultivar celebrated for its unmistakable candy-forward terpene profile. Often described as “smoking the rainbow,” this strain offers a mouthwatering burst of fruit candy, citrus, and tropical notes making it a favorite for daytime sessions, especially in the summer. While Zkittlez can be a challenging plant to grow with a finicky structure and lower-than-average vigor its end product more than makes up for the extra effort. The flavor, aroma, and overall smoking experience are unmatched, making it a must-have for connoisseurs and extract artists seeking standout terpene expression."},
    {"name": "Lemon Cherry Gelato", "price": 199.99, "description": "Lemon Cherry Gelato is a legendary hybrid born from the iconic Sunset Sherbet × Girl Scout Cookies lineage, with whispers that it may actually be a standout Runtz phenotype graciously passed on by the Runtz Crew to the Backpack Boyz for branding and cultivation. Developed in the Bay Area by Backpack Boyz, this exotic strain rapidly soared to fame thanks to its vibrant flavor and undeniable quality. Known for its vibrant appearance and loud candy gas terpene profile, this strain blends notes of sour lemon, ripe cherries, and creamy gelato. The buds are dense, colorful, and drenched in resin, making it a favorite for both flower and concentrate production. While its exact genetics are debated, the experience is unmistakable — a euphoric, flavor-packed smoke that leaves a lasting impression. Ideal for connoisseurs and hash makers alike, this cut brings both bag appeal and potency in one elite package."},
    {"name": "Blueberry Pancakes", "price": 99.99, "description": "Blueberry Pancakes by Humboldt Seed Co. is an exceptional strain that delivers an unforgettable experience. Bursting with pure blueberry terpenes, this cultivar is a true flavor powerhouse. Its dense, trichome-covered buds glisten with a heavy frost, making it as visually stunning as it is aromatic. A deliciously potent treat for flavor chasers and connoisseurs alike, Blueberry Pancakes is the perfect fusion of taste, potency, and top-shelf bag appeal."},
    {"name": "Mimosa", "price": 74.99, "description": "Mimosa is known for its uplifting effects and its crazy citrus aroma. A cross between Clementine and Purple Punch, this strain boasts dense, colorful buds coated in sparkling trichomes. Expect a refreshing burst of orange zest and tropical fruit on the nose, followed by a smooth, energetic high that’s perfect for daytime use. Whether you're looking to boost creativity, focus, or just brighten your mood, Mimosa delivers a flavorful and invigorating experience that lives up to its name."},
    {"name": "Purple Punch", "price": 74.99, "description": "Purple Punch by Symbiotic Genetics is a sweet and heavy-hitting indica-dominant hybrid (Larry OG x Granddaddy Purple). Known for its vibrant purple buds, grape candy aroma, and relaxing, full-body effects, it’s the perfect evening strain for easing stress, pain, and insomnia. With THC levels around 22%, Purple Punch delivers smooth sedation and dessert-like flavor in every puff."},
    {"name": "Yellow Guava", "price": 124.99, "description": "Yellow Guava is a sativa-leaning hybrid born from crossing Amarelo and Gassy Taffy by Symbiotic Genetics in collaboration with Lokey Farms. The lineage has a flavor profile combining the sweet, tropical essence suggested by Amarelo (meaning yellow) with the pungent, resinous character of Gassy Taffy. The result is a complex, aromatic experience that balances fruitiness with a bold, gassy undertone in a smooth, energizing high."},
    {"name": "Champaya", "price": 124.99, "description": "Champaya by Symbiotic Genetics is a sativa-leaning hybrid created from Papaya and Mimosa V6. It offers a smooth, tropical flavor with notes of ripe papaya, citrus, and a hint of earthiness. Known for its uplifting yet calming effects, Champaya delivers a clear-headed, enjoyable experience ideal for daytime use."},
    {"name": "Georgia Pie", "price": 99.99, "description": "Georgia Pie from Raw Genetics is a true expression of the Georgia Pie lineage, offering a rich mix of creamy Kush and earthy gas flavors. Its smooth, full-bodied taste blends creamy depth with a lingering gassy finish, leaving a lasting impression. The plants grow to a medium or tall height and produce dense, resin-coated buds with a striking aroma of creamy gas and Kush. This strain traces its genetics to well-known cultivars such as Gelato, Biscotti, Animal Mints, and Bubba Kush."},
    {"name": "Strawberry Cherry Gelato", "price": 99.99, "description": "Strawberry Cherry Gelato - Lemon Cherry Gelato X Strawberry Fritter by Raw Genetics brings together the fruity sweetness of Strawberry Fritter and the zesty citrus notes of Lemon Cherry Gelato to create a flavor-packed hybrid. This strain offers a rich profile featuring fresh strawberries, creamy pastry, and green apple tartness, perfectly balanced by bright lemon, sweet cherries, and a smooth gelato finish. It grows into medium to tall plants with dense, resin-coated buds that display vibrant green hues, deep purples, and sparkling trichomes. Genetically, Strawberry Cherry Gelato connects to iconic strains like OG, GSC, Animal Cookies, Sour Apple, Sherb, and Pink Panties, making it a standout in any lineup."},
    {"name": "Blueberry Pie", "price": 99.99, "description": "Blueberry Pie combines Blueberry Gushers X Georgia Pie for the gassy sweetness of Blueberry Gushers with the creamy Kush profile of Georgia Pie, delivering a potent hybrid with euphoric, relaxing effects. With tall plants, frost-coated flowers, and high yields, this strain offers both impressive performance and flavor."},
    {"name": "Blue Slushie", "price": 99.99, "description": "Blue Slushie is a sought-after indica hybrid by Raw Genetics that blends Blue Cookie with Georgia Pie, delivering rich flavors of vanilla cream, cookie dough, and sweet gas. Georgia Pie enhances the strain’s structure, supporting vigorous growth and large, dense colas while maintaining Blue Cookie’s signature frosty look. With genetics tied to Kush Mints, Gelatti, GSC, and OG Kush, Blue Slushie stands out as a flavorful and visually striking cultivar."},
    {"name": "Velvet Moon", "price": 99.99, "description": "Velvet Moon is the result of the famous Dosidos, crossed with one of the last breeding project made by Franco, the Holy Punch. The result is a great vigorous, and amazingly aesthetic plant with a very sweet and potent smell. The stretch is moderated, perfect for indoor and outdoor growers, with a very good branching on the side that can hold steady without support until the end of flowering."},
    {"name": "Super Silver Haze", "price": 74.99, "description": "Super Silver Haze is a legendary sativa-dominant strain known for its citrusy, spicy aroma and energizing, uplifting high. With THC levels up to 25%, it's perfect for daytime focus, creativity, and stress relief. A multiple Cannabis Cup winner with a strong Haze lineage."},
    {"name": "Super Lemon Haze", "price": 74.99, "description": "The Super Lemon Haze is a cross of the Lemon Skunk with the Famous Super Silver Haze. The result is a perfect combination of the two worlds: the strong high, compact flowers and terpene profile of the Lemon Skunk and the vigor, high-yielding flowers and typical Haze profile of the Super Silver Haze. A beautiful combination for all Sativa lovers and lemon addicts. Super Lemon Haze grows strong and vigorous in a Christmas-tree shape, with long and steady secondary branches ready to hold some weight. The branches will fill in the bud sites as the plant stretches, a stretch that can be pretty vigorous and at least double its size during flowering."},
    {"name": "Exodus Cheese", "price": 74.99, "description": "The Exodus Cheese is the original clone selected in the UK from the Skunk strain UK Cheese and feminized by Green House Seeds. The Exodus Cheese has a stretchy structure. If not topped regularly, it will produce many secondary branches, and the stem will be pretty thin and need support during flowering to hold the flowers. If topped properly, it will grow in a beautiful bushy structure."},
    {"name": "OREO BIG STUFF", "price": 99.99, "description": "As Seen in High Times (Mr.Big Stuff Copies breeder cut (Mac1 x Gary Payton) x Oreoz #3 reversal) epic bag appeal, with Large heavy yields, Epic frost monster, Indica dominant Heavy hitter. YIELD large, FLOWERING TIME 7-8 Weeks, TERPENE PROFILE: Candy, Gas, Strawberry, Vanilla cream."},
    {"name": "CANDYMAN", "price": 99.99, "description": "CandyMan is another original creation from Copy Cat Genetics (Watermelon Runtz Copies Cut x Oreo Big Stuff Copies High Times Legend cut, great bag appeal with heavy hard rock yields, frost monster, Super loud candy gassy terps, delicious potent smoke. FLOWERING TIME 56 days, TERPENE PROFILE: Sour Watermelon Candy, Fruity, Skunky, OG gas."},
    {"name": "IceBerry Muffinz", "price": 199.99, "description": "Ice Berry Muffin is the epitome of frosty, potent hybrids, crafted for those who crave both visual appeal and exceptional flavor. This indica-dominant masterpiece is a striking display of glistening trichomes, creating a snow-covered aesthetic that mirrors its name. The aroma and flavor transport you to the moment you unwrap a fresh blueberry muffin from Dunkin’ Donuts, with layers of sweet, baked blueberry goodness and subtle undertones of vanilla and cream."},
    {"name": "Sleeping Beauty", "price": 199.99, "description": "Sleeping Beauty is an original creation from CopyCat Genetics, bred by crossing Dr. Sleep with The Queen reversal. This strain delivers a heavy blend of gas, chem, and skunk aromas, living up to its name by offering deeply sedative effects. When harvested around day 56, it produces exceptionally high levels of CBN, making it ideal for nighttime use and promoting restful sleep."},
    {"name": "Slurricane #7", "price": 99.99, "description": "Slurricane #7 is the top-selected phenotype of Slurricane, handpicked by In House Genetics for its unbeatable combination of yield, resin, and rich flavor. A cross of Do-Si-Dos and Purple Punch, this standout cut delivers creamy berry terps, dense frosty buds, and a powerful, relaxing high. Chosen as the best expression of the line, it remains a favorite among growers and extractors alike."},
    {"name": "Jelly Breath", "price": 99.99, "description": "Jelly Breath S1 by In House Genetics (Jelly Breath (North Cascade Cut) × Jelly Breath) – Photoperiod Hybrid (50% Indica / 50% Sativa). Delivers super dense, frost-covered buds. Plants exhibit medium to tall stature, a flowering time of ~65 days, and medium yields."},
    {"name": "Sugar Cane", "price": 99.99, "description": "Sugar Cane by In House Genetics is a high-yielding hybrid created from Platinum and Slurricane. Known for its heavy resin production, it's a top choice for extractors, delivering dense, frosty buds with rich flavors of sweet grape, caramel, and subtle earth. The effects are uplifting and focused, making it ideal for daytime use, while the strain’s strong terpene profile and bag appeal make it a standout in any grow."},
    {"name": "BlackCherry Punch", "price": 99.99, "description": "Black Cherry Punch – In House Genetics (Black Cherry Pie × Purple Punch) is a visually stunning indica-dominant hybrid with deep purple buds, fiery pistils, and a thick frost of trichomes. It delivers a sweet berry and grape aroma with hints of spice and gas, making it a favorite for terp lovers and extractors alike. Expect a relaxing, euphoric body high paired with a gentle mental uplift — perfect for winding down or creative focus. Gorgeous bag appeal and consistent yields make this strain a hit with both growers and consumers."},
    {"name": "Strawberry Guava", "price": 99.99, "description": "Strawberry Guava by Bloom Seed Co (Strawberry Banana × Papaya) is a terp-heavy, indica-dominant hybrid known for its tropical guava-candy aroma and insane resin production. A favorite among hash makers, it washes over 4% to hash, making it ideal for water hash and rosin. Expect sweet, fruity flavor, heavy trichome coverage, and a chill, euphoric high that hits every time."},
    {"name": "Key Lime Guava", "price": 149.99, "description": "Key Lime Guava (Rainbow Guava #5 × TMZ) is a top-tier hash-washer bred for heavy resin output and intense tropical terps. With dominant notes of guava, lime, and creamy funk, this strain delivers both mouth-watering flavor and 4%+ wash returns in the right hands. Extract artists love its greasy trichome coverage, strong structure, and consistent yields across phenos. Whether you're pressing live rosin or running full-melt, Key Lime Guava is a must-have cultivar for solventless craft."},
    {"name": "Maple Drip", "price": 149.99, "description": "Maple Drip (OGKB 2.1 × Black Maple) is a solventless extractor’s dream, stacking greasy trichomes and 4%+ wash potential in the right environment. It delivers a rich maple syrup aroma layered with earthy gas and doughy funk, making it a standout in both flavor and yield. Dense buds, strong structure, and consistent resin returns make Maple Drip a top pick for hashmakers looking for unique terps and heavy output."},
    {"name": "Dulce de Papaya", "price": 149.99, "description": "Dulce de Papaya by Bloom Seed Co (Dulce de Uva x Papaya) amazing terps and great for water hash extract artists washes at over 4.1% to hash."},
    {"name": "Lemon Drip", "price": 99.99, "description": "Lemon Tree × Grease Monkey (aka Lemon Drip) by Exotic Genetix is a sativa-leaning hybrid known for its bright lemon and creamy gas flavor. With THC levels up to 28%, it delivers uplifting, focused effects and a rich terpene profile combining citrus, vanilla, and earthy kush. Flowering in 8–9 weeks, it’s a resin-heavy strain ideal for both flavor chasers and extractors."},
    {"name": "Milk & Cookies", "price": 99.99, "description": "Milk & Cookies by Exotic Genetix (Cookies & Cream × Triple OG) is a frost-covered indica hybrid with creamy vanilla, nutty, and gas-kissed terps. Its dense, resin-packed buds deliver excellent hash yields and rich flavor, making it a favorite for solventless extraction and terp chasers alike. Smooth, euphoric effects round out this dessert-style powerhouse."},
    {"name": "Twisted Terpz", "price": 99.99, "description": "Twisted Terpz by Exotic Genetix (Tropical Runtz × Grape Jubilee) is a vibrant 50/50 hybrid bursting with tropical fruit, grape, and sweet candy aromas. With potent 25–30% THC and an 8–9 week flowering time, it delivers a balanced high that blends uplifting creativity with smooth body relaxation. Expect dense, colorful buds and a flavor profile that keeps you coming back for more."},
    {"name": "Blueberry Gary", "price": 99.99, "description": "Blueberry Gary by Exotic Genetix is a potent hybrid crossing Gary Payton with Blueberry Bang Bang. It delivers bold flavors of sweet blueberry, earthy gas, and rubbery funk. With dense, frosty buds and a balanced high that’s both uplifting and relaxing, it’s a top-tier pick for flavor chasers and heavy-hitters alike. Finishes in 8–9 weeks."},
    {"name": "RS11", "price": 199.99, "description": "RS11, or Rainbow Sherbet #11, is a premium hybrid bred by Deep East, selected by Wizard Trees, and popularized by Doja Pak. Known for its vibrant terp profile of sweet fruit, gas, and candy, RS11 delivers a smooth, balanced high with strong visual appeal and heavy resin production."},
    {"name": "Strawberry Banana", "price": 74.99, "description": "Strawberry Banana by DNA Genetics is a high-THC, indica-dominant hybrid (Strawberry Banana × Strawberry Banana) bred for exceptional flavor, resin, and yield. Bursting with sweet strawberry, creamy banana, and subtle gas, this award-winning strain delivers euphoric, creative highs followed by deep relaxation. A favorite among both connoisseurs and extractors, it’s easy to grow and produces dense, trichome-rich buds in just 9 weeks. Expect 450–550g/m² indoors, with some phenos testing over 30% THC."},
    {"name": "Blue Dream", "price": 74.99, "description": "Blue Dream by DNA Genetics (Blueberry × Haze #1) is a sativa-dominant hybrid celebrated for its balanced head and body effects. Expect a creative, uplifting cerebral buzz that gracefully transitions into gentle full-body relaxation—perfect for daytime inspiration without the couch-lock. The flavor profile features sweet blueberry, soft vanilla, and herbal spice."},
    {"name": "GG4", "price": 49.99, "description": "The classic GG4 by DNA Genetics is a hard-hitting heavy yielding hybrid known for its intense potency, sticky resin. Loved by extractors for its heavy trichome output, GG4 is a top choice for both flower and concentrate production."}
]

# Featured clones (top 4, as in PHP code)
FEATURED_CLONES = CLONES[:4]

def clear():
    """Clear the console screen."""
    os.system("cls" if os.name == "nt" else "clear")

def typewriter(text, delay=0.02):
    """Print text with a typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def display_strain(strain, index=None):
    """Display a single strain's details."""
    clear()
    print("\033[94m" + BANNER + "\033[0m\n")  # Blue banner
    if index is not None:
        typewriter(f"\033[92m Strain {index + 1}/{len(CLONES)}: {strain['name']}\033[0m", 0.03)  # Green strain name
    else:
        typewriter(f"\033[92m Featured Strain: {strain['name']}\033[0m", 0.03)  # Green strain name
    typewriter(f"\033[93m Price: CA$ {strain['price']:.2f}\033[0m", 0.03)  # Yellow price
    typewriter(f"\033[97m Description: {strain['description']}\033[0m", 0.01)  # White description
    print("\n\033[96m Visit: https://exotic-clones.ca\033[0m\n")  # Cyan URL

def list_all_strains():
    """Display all strains one by one with user control."""
    try:
        for index, strain in enumerate(CLONES):
            display_strain(strain, index)
            input("\033[96mPress Enter to view next strain (or Ctrl+C to return to menu)...\033[0m")
    except KeyboardInterrupt:
        clear()
        print("\033[92mReturning to main menu...\033[0m")
        time.sleep(1)

def featured_loop():
    """Cycle through featured strains with user control."""
    try:
        for strain in itertools.cycle(FEATURED_CLONES):
            display_strain(strain)
            input("\033[96mPress Enter to view next featured strain (or Ctrl+C to return to menu)...\033[0m")
    except KeyboardInterrupt:
        clear()
        print("\033[92mReturning to main menu...\033[0m")
        time.sleep(1)

def main_menu():
    """Display the main menu and handle user input."""
    while True:
        clear()
        print("\033[94m" + BANNER + "\033[0m\n")
        typewriter("\033[92mWelcome to Exotic Clones - Premium Cannabis Clones in Canada\033[0m", 0.03)
        print("\033[96mPlease select an option:\033[0m")
        print("1. View All Strains")
        print("2. Cycle Through Featured Strains")
        print("3. Exit")
        print("\033[96m Visit: https://exotic-clones.ca\033[0m\n")
        
        choice = input("\033[93mEnter your choice (1-3): \033[0m").strip()
        
        if choice == "1":
            list_all_strains()
        elif choice == "2":
            featured_loop()
        elif choice == "3":
            clear()
            print("\033[91mThank you for visiting Exotic Clones! Goodbye!\033[0m")
            sys.exit(0)
        else:
            print("\033[91mInvalid choice. Please select 1, 2, or 3.\033[0m")
            time.sleep(2)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        clear()
        print("\033[91mExiting Exotic Clones Promo. Goodbye!\033[0m")
        sys.exit(0)

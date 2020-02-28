#!/usr/bin/env python3

# long_activity_generator.py
# Converts the IRS Form 1023/1024 ACTIVITY code in raw CSVs to human readable categories in a new column.
# Author:    Ru Uba (SavSanta)
# Created:   1.29.2020

import csv
from sys import argv, exit, exc_info

def process_data(row):
    ''' Strips the csv.DictReader data from tuplesets to writeable list values'''
    new_row = list(row.values())
    # Change the last column to the longform of activity names
    new_row[-1] = convertcode(new_row[col_index])
    return new_row

def convertcode(code):
    ''' Convert a IRS Form 1023/1024 ACTIVITY CODE to a organization category'''
    assert len(code) == 9
    long_activity = ""

    # Return a blank for all-zero data
    if code == "000000000":
        return ""

    for i in range(0, 9, 3):
        piece = code[i:i+3]
        # We prefix "||" in order to provide an uncommon punctuation sentinel to separate on
        long_activity +=  '||' + activity_dict[piece]

    return long_activity


# IRS Legend used for this hashmap source: -> EXEMPT ORGANIZATIONS BUSINESS MASTER FILE EXTRACT (EO BMF) April 2014 Edition
# It has a few caveats/bugs/issues:
# Category "000" added as there exists some data with only 1/3 or 2/3 of the nine-digit codes not being 000. (e.g. 059000000 - )
# Category "999" added because it makes an appearance once but also isnt defined
# There is an "Unspecified" category (Key "998") that doesnt seem to be used.

activity_dict = {

    "000" : "",
    "999" : "",
    "001" : "Church, synagogue, etc",
    "002" : "Association or convention of churches",
    "003" : "Religious order",
    "004" : "Church auxiliary",
    "005" : "Mission",
    "006" : "Missionary activities",
    "007" : "Evangelism",
    "008" : "Religious publishing activities",
    "029" : "Other religious activities",
    "030" : "School, college, trade school, etc.",
    "031" : "Special school for the blind, handicapped, etc",
    "032" : "Nursery school",
    "033" : "Faculty group",
    "034" : "Alumni association or group",
    "035" : "Parent or parent-teachers association",
    "036" : "Fraternity or sorority",
    "037" : "Other student society or group",
    "038" : "School or college athletic association",
    "039" : "Scholarships for children of employees",
    "040" : "Scholarships (other)",
    "041" : "Student loans",
    "042" : "Student housing activities",
    "043" : "Other student aid",
    "044" : "Student exchange with foreign country",
    "045" : "Student operated business",
    "046" : "Private school",
    "059" : "Other school related activities",
    "060" : "Museum, zoo, planetarium, etc.",
    "061" : "Library",
    "062" : "Historical site, records or reenactment",
    "063" : "Monument",
    "064" : "Commemorative event (centennial, festival, pageant, etc.)",
    "065" : "Fair",
    "088" : "Community theatrical group",
    "089" : "Singing society or group",
    "090" : "Cultural performances",
    "091" : "Art exhibit",
    "092" : "Literary activities",
    "093" : "Cultural exchanges with foreign country",
    "094" : "Genealogical activities",
    "119" : "Other cultural or historical activities",
    "120" : "Publishing activities",
    "121" : "Radio or television broadcasting",
    "122" : "Producing films",
    "123" : "Discussion groups, forums, panels lectures, etc.",
    "124" : "Study and research (non-scientific)",
    "125" : "Giving information or opinion (see also Advocacy)",
    "126" : "Apprentice training",
    "149" : "Other instruction and training",
    "150" : "Hospital",
    "151" : "Hospital auxiliary",
    "152" : "Nursing or convalescent home",
    "153" : "Care and housing for the aged (see also 382)",
    "154" : "Health clinic",
    "155" : "Rural medical facility",
    "156" : "Blood bank",
    "157" : "Cooperative hospital service organization",
    "158" : "Rescue and emergency service",
    "159" : "Nurses register or bureau",
    "160" : "Aid to the handicapped (see also 031)",
    "161" : "Scientific research (diseases)",
    "162" : "Other medical research",
    "163" : "Health insurance (medical, dental, optical, etc.)",
    "164" : "Prepared group health plan",
    "165" : "Community health planning",
    "166" : "Mental health care",
    "167" : "Group medical practice association",
    "168" : "In-faculty group practice association",
    "169" : "Hospital pharmacy, parking facility, food services, etc.",
    "179" : "Other health services",
    "180" : "Contact or sponsored scientific research for industry",
    "181" : "Scientific research for government",
    "199" : "Other scientific research activities",
    "200" : "Business promotion (chamber of commerce, business league, etc.",
    "201" : "Real estate association",
    "202" : "Board of trade",
    "203" : "Regulating business",
    "204" : "Promotion of fair business practices",
    "205" : "Professional association",
    "206" : "Professional association auxiliary",
    "207" : "Industry trade shows",
    "208" : "Convention displays",
    "209" : "Research, development and testing",
    "210" : "Professional athletic league",
    "211" : "Underwriting municipal insurance",
    "212" : "Assigned risk insurance activities",
    "213" : "Tourist bureau",
    "229" : "Other business or professional group",
    "230" : "Farming",
    "231" : "Farm bureau",
    "232" : "Agricultural group",
    "233" : "Horticultural group",
    "234" : "Farmers cooperative marketing or purchasing",
    "235" : "Farmers cooperative marketing or purchasing",
    "236" : "Dairy herd improvement association",
    "237" : "Breeders association",
    "249" : "Other farming and related activities",
    "250" : "Mutual ditch, irrigation, telephone, electric company or like organization",
    "251" : "Credit union",
    "252" : "Reserve funds or insurance for domestic building and loan association, cooperative bank, or mutual savings bank",
    "253" : "Mutual insurance company",
    "254" : "Corporation organized under an Act of Congress (see also use (904)",
    "259" : "Other mutual organization",
    "260" : "Fraternal Beneficiary society, order, or association",
    "261" : "Improvement of conditions of workers",
    "262" : "Association of municipal employees",
    "263" : "Association of employees",
    "264" : "Employee or member welfare association",
    "265" : "Sick, accident, death, or similar benefits",
    "266" : "Strike benefits",
    "267" : "Unemployment benefits",
    "268" : "Pension or retirement benefits",
    "269" : "Vacation benefits",
    "279" : "Other services or benefits to members or employees",
    "280" : "Country club",
    "281" : "Hobby club",
    "282" : "Dinner club",
    "283" : "Variety club",
    "284" : "Dog club",
    "285" : "Women's club",
    "286" : "Hunting or fishing club",
    "287" : "Swimming or tennis club",
    "288" : "Other sports club",
    "296" : "Community center",
    "297" : "Community recreational facilities (park, playground, etc)",
    "298" : "Training in sports",
    "299" : "Travel tours",
    "300" : "Amateur athletic association",
    "301" : "Fundraising athletic or sports event",
    "317" : "Other sports or athletic activities",
    "318" : "Other recreational activities",
    "319" : "Other social activities",
    "320" : "Boy Scouts, Girl Scouts, etc.",
    "321" : "Boys Club, Little League, etc.",
    "322" : "FFA, FHA, 4-H club, etc.",
    "323" : "Key club",
    "324" : "YMCA, YWCA, YMCA, etc.",
    "325" : "Camp",
    "326" : "Care and housing of children (orphanage, etc)",
    "327" : "Prevention of cruelty to children",
    "328" : "Combat juvenile delinquency",
    "349" : "Other youth organization or activities",
    "350" : "Preservation of natural resources (conservation)",
    "351" : "Combating or preventing pollution (air, water, etc)",
    "352" : "Land acquisition for preservation",
    "353" : "Soil or water conservation",
    "354" : "Preservation of scenic beauty",
    "355" : "Wildlife sanctuary or refuge",
    "356" : "Garden club",
    "379" : "Other conservation, environmental or beautification activities",
    "380" : "Low-income housing",
    "381" : "Low and moderate income housing",
    "382" : "Housing for the aged (see also 153)",
    "398" : "Instruction and guidance on housing",
    "399" : "Other housing activities",
    "400" : "Area development, redevelopment of renewal",
    "401" : "Homeowners association",
    "402" : "Other activity aimed t combating community deterioration",
    "403" : "Attracting new industry or retaining industry in an area",
    "404" : "Community promotion",
    "405" : "Loans or grants for minority businesses",
    "406" : "Crime prevention",
    "407" : "Voluntary firemen's organization or auxiliary",
    "408" : "Community service organization",
    "429" : "Other inner city or community benefit activities",
    "430" : "Defense of human and civil rights",
    "431" : "Elimination of prejudice and discrimination (race, religion, sex, national origin, etc)",
    "432" : "Lessen neighborhood tensions",
    "449" : "Other civil rights activities",
    "460" : "Public interest litigation activities",
    "461" : "Other litigation or support of litigation",
    "462" : "Legal aid to indigents",
    "463" : "Providing bail",
    "465" : "Plan under IRC section 120 ",
    "480" : "Propose, support, or oppose legislation",
    "481" : "Voter information on issues or candidates",
    "482" : "Voter education (mechanics of registering, voting etc.)",
    "483" : "Support, oppose, or rate political candidates",
    "484" : "Provide facilities or services for political campaign activities",
    "509" : "Other legislative and political activities",
    "510" : "Firearms control",
    "511" : "Selective Service System",
    "512" : "National defense policy",
    "513" : "Weapons systems",
    "514" : "Government spending",
    "515" : "Taxes or tax exemption",
    "516" : "Separation of church and state",
    "517" : "Government aid to parochial schools",
    "518" : "U.S. foreign policy",
    "519" : "U.S. military involvement",
    "520" : "Pacifism and peace",
    "521" : "Economic-political system of U.S.",
    "522" : "Anti-communism",
    "523" : "Right to work",
    "524" : "Zoning or rezoning",
    "525" : "Location of highway or transportation system",
    "526" : "Rights of criminal defendants",
    "527" : "Capital punishment",
    "528" : "Stricter law enforcement",
    "529" : "Ecology or conservation",
    "530" : "Protection of consumer interests",
    "531" : "Medical care service",
    "532" : "Welfare systems",
    "533" : "Urban renewal",
    "534" : "Busing student to achieve racial balance",
    "535" : "Racial integration",
    "536" : "Use of intoxicating beverage",
    "537" : "Use of drugs or narcotics",
    "538" : "Use of tobacco",
    "539" : "Prohibition of erotica",
    "540" : "Sex education in public schools",
    "541" : "Population control",
    "542" : "Birth control methods",
    "543" : "Legalized abortion",
    "559" : "Other matters",
    "560" : "Supplying money, goods or services to the poor",
    "561" : "Gifts or grants to individuals (other than scholarships)",
    "562" : "Other loans to individuals",
    "563" : "Marriage counseling",
    "564" : "Family planning",
    "565" : "Credit counseling and assistance",
    "566" : "Job training, counseling, or assistance",
    "567" : "Draft counseling",
    "568" : "Vocational counseling",
    "569" : "Referral service (social agencies)",
    "572" : "Rehabilitating convicts or ex-convicts",
    "573" : "Rehabilitating alcoholics, drug abusers, compulsive gamblers, etc.",
    "574" : "Day care center",
    "575" : "Services for the aged (see also 153 ad 382)",
    "600" : "Community Chest, United Way, etc.",
    "601" : "Booster club",
    "602" : "Gifts, grants, or loans to other organizations",
    "603" : "Non-financial services of facilities to other organizations",
    "900" : "Cemetery or burial activities",
    "901" : "Perpetual (care fund (cemetery, columbarium, etc)",
    "902" : "Emergency or disaster aid fund",
    "903" : "Community trust or component",
    "904" : "Government instrumentality or agency (see also 254)",
    "905" : "Testing products for public safety",
    "906" : "Consumer interest group",
    "907" : "Veterans activities",
    "908" : "Patriotic activities",
    "909" : "Non-exempt charitable trust described in section 4947(a)(1) of the Code",
    "910" : "Domestic organization with activities outside U.S.",
    "911" : "Foreign organization",
    "912" : "Title holding corporation",
    "913" : "Prevention of cruelty to animals",
    "914" : "Achievement pries of awards",
    "915" : "Erection or maintenance of public building or works",
    "916" : "Cafeteria, restaurant, snack bar, food services, etc.",
    "917" : "Thrift ship, retail outlet, etc.",
    "918" : "Book, gift or supply store",
    "919" : "Advertising",
    "920" : "Association of employees",
    "921" : "Loans or credit reporting",
    "922" : "Endowment fund or financial services",
    "923" : "Indians (tribes, cultures, etc.)",
    "924" : "Traffic or tariff bureau",
    "925" : "Section 501(c)(1) with 50% deductibility",
    "926" : "Government instrumentality other than section 501(c)",
    "927" : "Fundraising",
    "928" : "4947(a)(2) trust",
    "930" : "Prepaid legal services pan exempt under IRC section 501(c)(20)",
    "931" : "Withdrawal liability payment fund",
    "990" : "Section 501(k) child care organization",
    "994" : "Described in section 170(b)1)(a)(vi) of the Code",
    "995" : "Described in section 509(a)(2) of the Code",
    "998" : "Unspecified"
}

# Ensure that this program was passed a valid filename on the commandline
if len(argv) != 2:
    print("ERROR!")
    print("USAGE: long_activity_generator.py [/path/to/convert.csv]")
    exit(-1)
else:
    filename = argv[1]
    outfilename = filename[0:-4] + "+LONG_ACTIVITY_COL.csv"
    print("Working on conversion ---> {}".format(filename))

    try:
        # Open file handles with special flags to avoid OS quirks.
        f = open(filename, "rU")
        fw = open(outfilename, "w", newline='')

        # Use csv reader object to read the filename and convert content to a DictReader obj.
        # Note: Doesnt attempt to account for manipulated format data from non-raw CSVs.
        reader = csv.DictReader(f)
        writer = csv.writer(fw)

        # Ensure this is the correct file, by testing if header content has an 'ACTIVITY' column
        try:
            col_names = reader.fieldnames
            col_index = col_names.index("ACTIVITY")
            print("Found 'ACTIVITY' column in position {}".format(col_index))
        except ValueError:
            print("ERROR! Missing 'ACTIVITY' column header in csv!")
            exit(-2)
        else:
            col_names.append("ACTIVITY_FULL")
            writer.writerow(col_names)

        # Call functions to modify the data and write to new csv file.
        for row in reader:
            writer.writerow(process_data(row))
        print("Conversion completed ---> {}".format(outfilename))

    except (IOError, FileNotFoundError) as e:
        print("ERROR accessing file: {}".format(filename))
        raise
    except:
        print("Unexpected ERROR --> " + exc_info()[0].__name__)
        raise
    else:
        # Close open handles
        f.close()
        fw.close()




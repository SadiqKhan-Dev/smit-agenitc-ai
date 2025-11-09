# student_data = [
#      {
#         "id" : 523169,
#         "name" : "Ahnaf" ,
#         "age" : 16 ,
#         "course" : ["Web & App", "Agentic Ai", "Ai Digital Marketing"] ,
#     }
# ]
# print(student_data[0])

# pizza_prise: int = 32

# continue  (pizza_prise ===  32) {
#     print("You can get the pizza")
# } break {
#     print("sorry for the prize")
# }

# number1 = int(input("Enter Your First Number: "))
# number2 = int(input("Enter Your Second Number: "))


# print("The Sum of Two number is :" , number1 + number2)

# print("*_" * 9)
# sub

# number3 = int(input("Enter Your First Number: "))
# number4 = int(input("Enter Your Second Number: "))


# print("The Sum of Two number is :" , number3 - number4)

# number3 = int(input("Enter Your First Number: "))
# number4 = int(input("Enter Your Second Number: "))


# print("The Sum of Two number is :" , number3 - number4)

# number3 = int(input("Enter Your First Number: "))
# number4 = int(input("Enter Your Second Number: "))


# print("The Sum of Two number is :" , number3 - number4)

# print("*_" * 60)

# 


# number5 = int(input("Enter Your First Number: "))
# number6 = int(input("Enter Your Second Number: "))


# # print("The Sum of Two number is :" , number5 * number6)
# print("*_" * 80)

# # number7 = int(input("Enter Your First Number: "))
# # number8 = int(input("Enter Your Second Number: "))


# # print("The Sum of Two number is :" , number7 // number8)


# print("*_" * 80)

# x = 4
# y = 1
# x,y = y,x
# print(x, y)

# Creating an Excel (.xlsx) file with the 20 verified venues and contact details gathered.
import pandas as pd

data = [
    ["Paradise Village Venue", "Ashford, WA", "myvenue@paradisevillagelodge.com", "(425) 534-4036", "https://www.paradisevillagevenue.com", "Source: venue contact page"],
    ["Thornewood Castle", "Lakewood, WA", "info@thornewoodcastle.com", "(253) 584-4393", "https://www.thornewoodcastle.com", "Source: venue contact page"],
    ["Lake Quinault Lodge", "Quinault, WA", "", "(360) 288-2910", "https://www.olympicnationalparks.com/meetings-events/lake-quinault-lodge/", "Managed by Aramark; no public email on site"],
    ["The Edgewater Hotel", "Seattle, WA", "edgeweddings@edgewaterhotel.com", "(206) 971-5703", "https://www.edgewaterhotel.com", "Weddings contact"],
    ["Columbia Tower Club", "Seattle, WA", "", "(206) 622-2010", "https://www.invitedclubs.com/clubs/columbia-tower-club", "Contact via club portal / inquiry form"],
    ["Semiahmoo Resort Golf and Spa", "Blaine, WA", "info@semiahmoo.com", "(360) 318-2000", "https://semiahmoo.com", "Resort contact"],
    ["McMenamins Anderson School", "Bothell, WA", "", "(425) 398-0127", "https://www.mcmenamins.com/anderson-school", "Event & weddings contact on site"],
    ["Chuckanut Bay Distillery", "Bellingham, WA", "", "(360) 738-7179", "https://chuckanutbaydistillery.com", "Distillery contact page"],
    ["Saltwater Farm at Friday Harbor", "Friday Harbor, WA", "info@saltwaterfarmSJI.com", "(360) 317-6339", "https://www.saltwaterfarmsji.com", "Venue contact page"],
    ["theBindery (Tacoma)", "Tacoma, WA", "info@thebinderywa.com", "253-753-1928", "https://www.thebinderywa.com", "Venue contact / tour page"],
    ["Hilton Bellevue", "Bellevue, WA", "LION_FO@hilton.com", "(425) 455-1300", "https://www.hilton.com/en/hotels/lion-hf-hilton-bellevue/", "Hotel main contact"],
    ["SoDo Park by Landmark Event Co", "Seattle, WA", "", "(206) 222-1175", "https://landmarkeventco.com/venues/sodo-park/", "Landmark Event Co venue; contact via Landmark"],
    ["Hyatt Regency Lake Washington", "Renton, WA", "searl.rfp@hyatt.com", "(425) 203-1234", "https://www.hyatt.com/hyatt-regency/en-US/searl-hyatt-regency-lake-washington-at-seattles-southport", "Weddings / RFP contact"],
    ["The Woodmark Hotel & Still Spa", "Kirkland, WA", "celebrate@woodmarkkirkland.com", "425-827-1986", "https://www.thewoodmark.com", "Weddings contact"],
    ["Canterwood Golf & Country Club", "Gig Harbor, WA", "", "253-851-1845", "https://www.canterwood.org", "Clubhouse phone listed"],
    ["City Farm Chehalis", "Chehalis, WA", "info@cityfarmchehalis.com", "310-913-1889", "https://www.cityfarmchehalis.com", "Contact form & hire-us page"],
    ["Blue Boy West Golf Course & Event Center", "Monroe, WA", "events@blueboywest.com", "(360) 793-2378", "https://www.blueboywest.com", "Events contact"],
    ["The Lodge at St. Edward", "Kenmore, WA", "info@thelodgeatstedward.com", "425-470-6500", "https://www.thelodgeatstedward.com", "Venue contact"],
    ["Genesis Farm & Gardens", "Enumclaw, WA", "", "425-654-1385", "https://www.genesisfarmandgardens.com", "Contact page lists phone"],
    ["Fremont Foundry (Landmark Event Co)", "Seattle, WA", "", "(206) 588-6981", "https://landmarkeventco.com/venues/fremont-foundry/", "Landmark Event Co venue (phone from VisitSeattle)"]
]

df = pd.DataFrame(data, columns=["Venue Name", "City", "Email", "Phone", "Website", "Notes"])

# Save to Excel
file_path = "/mnt/data/washington_wedding_venues_contacts.xlsx"
df.to_excel(file_path, index=False)

# Display table to user
from caas_jupyter_tools import display_dataframe_to_user
display_dataframe_to_user("Washington wedding venues (verified contacts)", df)

# Provide the download path
file_path




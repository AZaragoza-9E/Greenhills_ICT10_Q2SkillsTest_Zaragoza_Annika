# Working with Dictionaries
from pyscript import display, document


monarch_club = {
    'Name': "Monarch Club",
    'Description' : "A pulse-pounding fusion of rhythm, lights, and social energy. The perfect place to move, connect, and feel alive.",
    'Time': "Every Monday and Thursday 3-5 PM",
    'Adviser' : "Mr. Marutani",
    'Number of Members' : "20",
    'Category' : "Cultural"
}

cocc_club = {
    'Name': "COCC Club",
    'Description' : "We offer a supportive, military-inspired environment where members learn teamwork, resilience, and strong character.",
    'Time': "Every Monday and Tuesday 3-5 PM",
    'Adviser' : "Mr. Dela Peña",
    'Number of Members' : "20",
    'Category' : "Academic"
}


glee_club = {
    'Name': "Glee Club",
    'Description' : "A creative space for vocal expression, we unite passionate singers to collaborate, grow, and shine on stage.",
    'Time': "Every Monday and Wednesday 3-5 PM",
    'Adviser' : "Ms. Loyola",
    'Number of Members' : "20",
    'Category' : "Cultural"
}


art_club = {
    'Name': "Art Club",
    'Description' : "A space for imagination and craftsmanship, we bring together creators to experiment, collaborate, and make meaningful art.",
    'Time': "Every Monday and Friday 3-5 PM",
    'Adviser' : "Ms. Suarez",
    'Number of Members' : "20",
    'Category' : "Cultural"
}

club_map = {
    "Monarch Club": monarch_club,
    "COCC Club": cocc_club,
    "Glee Club": glee_club,
    "Art Club": art_club
}


def displayinfo(e): #sofia ty for helping mee T-T 

    e.preventDefault()
    club_selection = document.getElementById("club-select").value
    club = club_map.get(club_selection, {})

    info = f"""
    <h2>{club.get('Name')}</h2>
    <p>Description: {club.get('Description')}</p>
    <p>Time: {club.get('Time')}</p>
    <p>Advisor: {club.get('Adviser')}</p>
    <p>Number of Members: {club.get('Number of Members')}</p>
    <p>Category: {club.get('Category')}</p>
    """

    document.getElementById("clubinformation").innerHTML = info



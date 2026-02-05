"""
College Enquiry Chatbot
A helpful assistant to answer student and parent queries about the college.
Chatbot Name: Sweety
"""

import datetime

college_info = {
    "courses": [
        "Bachelor of Technology (B.Tech) - Computer Science",
        "Bachelor of Technology (B.Tech) - Mechanical Engineering",
        "Bachelor of Technology (B.Tech) - Electrical Engineering",
        "Bachelor of Science (B.Sc) - Physics",
        "Bachelor of Science (B.Sc) - Chemistry",
        "Bachelor of Arts (B.A) - English Literature"
    ],
    "admission": "You can apply online through our college website. Submit your application with required documents by the deadline. Admission is based on merit and entrance exam scores.",
    "eligibility": "For B.Tech: 12th pass with Math and Physics. For B.Sc and B.A: 12th pass with relevant subjects. Minimum 50% aggregate required.",
    "fees": {
        "btech": "₹5,00,000 per year",
        "bsc": "₹2,00,000 per year",
        "ba": "₹1,50,000 per year"
    },
    "hostel": {
        "availability": "Yes, separate hostels for boys and girls",
        "capacity": "500 students total",
        "facilities": ["WiFi", "Mess facility", "24/7 Security", "Sports facilities", "Study rooms"]
    },
    "timings": "Classes: 8:00 AM - 5:00 PM (Monday-Friday), Library: 7:00 AM - 9:00 PM, Hostels: Open 24/7",
    "placement": {
        "average_package": "₹6.5 LPA",
        "highest_package": "₹15 LPA",
        "companies": ["TCS", "Infosys", "Google", "Microsoft", "Amazon"],
        "placement_rate": "95%"
    },
    "contact": {
        "phone": "+91-1234-567890",
        "email": "admissions@college.edu",
        "address": "123 Education Street, City, State 000000",
        "website": "www.college.edu"
    }
}

user_name = ""
query_count = 0

def get_time_greeting():
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Good Morning"
    elif hour < 17:
        return "Good Afternoon"
    else:
        return "Good Evening"

def get_course_info():
    courses = "\n".join([f"• {course}" for course in college_info["courses"]])
    return f"We offer the following courses:\n{courses}"

def get_admission_info():
    return f"Admission Process:\n{college_info['admission']}"

def get_eligibility_info():
    return f"Eligibility Criteria:\n{college_info['eligibility']}"

def get_fee_info():
    fees_text = "\n".join([f"• {key.upper()}: {value}" for key, value in college_info["fees"].items()])
    return f"Fee Structure:\n{fees_text}"

def get_hostel_info():
    facilities = "\n".join([f"• {facility}" for facility in college_info["hostel"]["facilities"]])
    return (
        f"Hostel Facilities:\n"
        f"Availability: {college_info['hostel']['availability']}\n"
        f"Capacity: {college_info['hostel']['capacity']} students\n\n"
        f"Facilities:\n{facilities}"
    )

def get_timings_info():
    return f"College Timings:\n{college_info['timings']}"

def get_placement_info():
    companies = ", ".join(college_info['placement']['companies'])
    return (
        f"Placement Details:\n"
        f"• Average Package: {college_info['placement']['average_package']}\n"
        f"• Highest Package: {college_info['placement']['highest_package']}\n"
        f"• Placement Rate: {college_info['placement']['placement_rate']}\n"
        f"• Top Recruiting Companies: {companies}"
    )

def get_contact_info():
    return (
        "Contact Information:\n"
        f"• Phone: {college_info['contact']['phone']}\n"
        f"• Email: {college_info['contact']['email']}\n"
        f"• Address: {college_info['contact']['address']}\n"
        f"• Website: {college_info['contact']['website']}"
    )

def process_query(user_input):
    global query_count
    query_count += 1

    user_input = user_input.lower().strip()

    if any(word in user_input for word in ["course", "program", "degree"]):
        return get_course_info()

    elif any(word in user_input for word in ["admission", "apply", "application"]):
        return get_admission_info()

    elif any(word in user_input for word in ["eligible", "eligibility", "requirement", "qualify"]):
        return get_eligibility_info()

    elif any(word in user_input for word in ["fee", "fees", "cost", "price", "tuition"]):
        return get_fee_info()

    elif any(word in user_input for word in ["hostel", "accommodation", "room", "stay"]):
        return get_hostel_info()

    elif any(word in user_input for word in ["timing", "time", "schedule", "class"]):
        return get_timings_info()

    elif any(word in user_input for word in ["placement", "job", "salary", "company"]):
        return get_placement_info()

    elif any(word in user_input for word in ["contact", "call", "phone", "email", "address"]):
        return get_contact_info()

    elif any(word in user_input for word in ["hello", "hi", "hey"]):
        return f"Namaste 🙏 {user_name}! Main Sweety bol rahi hoon 😊 Aap kya jaanna chahenge?"

    elif any(word in user_input for word in ["thank", "thanks"]):
        return "Aapka swagat hai 😊 Aur koi sawal ho toh poochiye."

    elif user_input in ["?", "help"]:
        return (
            "Main aapki madad kar sakti hoon in topics par:\n"
            "• Courses\n• Admission\n• Eligibility\n• Fees\n• Hostel\n"
            "• Timings\n• Placements\n• Contact Details"
        )

    else:
        return (
            "Mujhe lagta hai aap kuch aur poochna chah rahe hain 🤔\n"
            "Try keywords like: courses, admission, fees, hostel, placement"
        )

def display_welcome_message():
    global user_name

    print("\n" + "=" * 60)
    print("🌸 Namaste 🙏 | Raadhe Raadhe 🌸")
    print("Welcome to College Enquiry Chatbot")
    print("Chatbot Name: Sweety 🤖")
    print("=" * 60)

    time_greet = get_time_greeting()
    print(f"\n{time_greet}! Main Sweety hoon 😊")
    user_name = input("Sweety: Aapka naam kya hai? 😊\nYou: ").strip() or "Friend"

    print(f"\nSweety: Bahut achha laga {user_name}! 💐")
    print("Main aapke college se jude har sawal ka jawab dungi.")
    print("\nType '?' or 'help' for options.")
    print("Type 'exit' or 'quit' to end the chat.")
    print("=" * 60 + "\n")

def main():
    display_welcome_message()

    while True:
        try:
            user_query = input("You: ").strip()

            if user_query.lower() in ["exit", "quit", "bye"]:
                print(
                    f"\nSweety: Dhanyavaad {user_name}! 💖\n"
                    f"Aapne total {query_count} sawal pooche.\n"
                    "Best wishes for your bright future 🌟"
                )
                print("=" * 60)
                break

            if not user_query:
                continue

            response = process_query(user_query)
            print(f"\nSweety: {response}\n")

        except KeyboardInterrupt:
            print("\nSweety: Alvida! Aapse baat karke achha laga 😊")
            break

if __name__ == "__main__":
    main()

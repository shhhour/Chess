import streamlit as st

# Set the title of the app
st.title("Student Chess Network (SCN)")

# Sidebar for navigation
page = st.sidebar.selectbox("Select a page", ["Home", "About Us", "Programs", "Sign Up"])

# Home Page
if page == "Home":
    st.header("Welcome to the Student Chess Network (SCN)!")
    st.write("""
        SCN is a student-run chess organization that hosts private chess classes (online and in person), 
        group lessons, tournaments, and camps during the year. Learning to play chess offers students an 
        opportunity to sharpen their intellect and develop essential life skills. The game is a powerful 
        tool for enhancing critical thinking, strategic planning, and decision-making under pressure. 
        Each move requires thorough analysis and foresight, encouraging players to weigh consequences 
        and anticipate outcomes. Beyond cognitive benefits, chess also fosters patience, discipline, 
        and resilience—qualities that translate to academic and personal success. As students navigate 
        complex challenges both on and off the board, chess equips them with a mindset of perseverance 
        and ability to make wise decisions, making it a valuable addition to a child’s growth.
    """)
    st.image("path_to_logo.png")  # Replace with your logo path
    st.image("path_to_shouri_trophy.png")  # Replace with your trophy image path
    st.image("path_to_dhairya_trophy.png")  # Replace with Dhairya's trophy image path
    st.write("""
        **Quote:** Life is like a game of chess. To win you have to make a move knowing which move to 
        make comes with in-sight and knowledge and by learning lessons that are accumulated along the way. 
        We become each and every piece within the game called Life - Allan Rufus.
    """)

    
# About Us Page
elif page == "About Us":
    st.header("About Us (Founders)")
    
    st.subheader("Shouri Mosaliganti (Fundamentals Coach 0-1000 USCF)")
    st.write("""
        I started chess by watching my father and gaining curiosity, joining a chess camp and learning 
        the basics while competing in small tournaments. I began taking private lessons and gained 1600 
        USCF rating points within two years, captained two school teams to back-to-back state championship 
        titles, placed in the top 5 best players in the country (for age), won over $5000 in tournament, 
        have coached chess for over 4 years, and am a certified Tournament Director.
    """)
    st.image("path_to_shouri_trophy.png")  # Replace with your trophy image path

    st.subheader("Dhairya Mehta (Intermediate and Advanced Coach 1000-1800 USCF)")
    st.write("""
        From a birthday gift to a lifelong passion, my chess journey began at age five when I received 
        a chessboard that sat unopened for months. I asked my father to teach me the rules and by age 
        six, I was competing in my first tournament paving my path to a USCF rating of 2160, a 4 time 
        state champion, 2 winner of the spiegel cup, a top 10 chess player in the country (for age), 
        a certified tournament director, and chess events organizer in my local community.
    """)
    st.image("path_to_dhairya_trophy.png")  # Replace with Dhairya's trophy image path

    st.write("""
        **Quote:** “Life is like a chess game. It’s not about the pieces but it’s about how you move them.”
    """)


# Programs Page
elif page == "Programs":
    st.header("Programs")
    
    st.subheader("Private Classes (One on One)")
    st.write("""
        Our private lessons are the most popular classes, geared for students that want personalized 
        training, targeting specific weaknesses with an assigned coach purposed for long term development. 
        We give weekly lessons (1 hour each week) charging $35 for each lesson or $120 per month. 
        Once in contact with a coach, details regarding in-person or online and timings can be figured out.
    """)
    st.image("path_to_dhairya_coaching.png")  # Replace with coaching image path

    st.subheader("Camps")
    st.write("""
        We host annual Summer Chess Camps for kids of all ages and skill levels, offering both full-day 
        (9:00 AM – 3:00 PM, $400/week) and half-day (9:00 AM – 12:00 PM, or 12:00 PM- PM, $250/week) 
        options. Each day is packed with group lessons customized to different abilities, puzzle challenges, 
        chess-related activities like bughouse, blitz games, chess art, and small tournaments. Beyond the 
        board, we emphasize teamwork and community-building through collaborative exercises, outdoor play, 
        coach-led simuls, and team games. 
        Location: 146 E Main St, Hopkinton, MA 01748 - August 11-15, 2025.
    """)

    st.subheader("Group Lessons")
    st.write("""
        Our group classes contain roughly 4-6 kids with prices as $20 for each class or $70 a month. 
        We have two levels (0-1000) and (1000-1500), focused on analyzing student games and teaching 
        crucial concepts in all three phases of the game. This option is better for younger kids due to 
        the blend of fun and social interaction with learning, aimed to boost the interest in the game.
    """)

    st.subheader("Tournaments")
    st.write("""
        We run tournaments every other month in the Boylston Chess Club (35 Kingston St STE 1, Boston, MA 02111). 
        These tournaments are usually 4 round swiss tournaments or quads, costing $20-30 per tournament. 
        In the Swiss there are three sections, U1000, U1600, and Open.
    """)


# Sign Up Page
elif page == "Sign Up":
    st.header("Sign Up")
    st.write("Sign up for any of our services here!")
    
    with st.form("signup_form"):
        full_name_child = st.text_input("Full Name (Child) *")
        full_name_parent = st.text_input("Full Name (Parent or Guardian)")
        contact_info = st.text_input("Phone Number / Email (Parent or Student)")
        skill_level = st.selectbox("Skill Level of the Child", 
                                    ["Beginner (Knows the Basics)", 
                                     "Beginner Advanced (Plays Online)", 
                                     "Intermediate (Started Playing USCF tournaments)", 
                                     "Advanced (Regular Player in Tournaments)"])
        uscf_rating = st.text_input("If rated, what is your current USCF/FIDE rating?")
        interests = st.multiselect("What are you interested in?", 
                                    ["Summer Camp", "Group Lessons", "Private Lessons", "Tournaments"])
        availability = st.multiselect("What is your availability?", 
                                       ["Before 4 PM", "4 PM - 5 PM", "5 PM - 6 PM", 
                                        "6 PM - 7 PM", "7 PM - 8 PM", "8 PM - 9 PM"],
                                       default=["Before 4 PM"])
        private_class_type = st.selectbox("If interested in private classes", 
                                           ["In-person (Rates start at $40 an hour)", 
                                            "Online (Rates start at $30 an hour)", "Other:"])
        questions = st.text_area("Do you have any questions for us?")
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("Thank you for signing up! We will get back to you soon.")


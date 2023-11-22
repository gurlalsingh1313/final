import streamlit as st

def page_home():
     st.title("About this Project - FitWithTech")
     st.write("Welcome to our comprehensive fitness and nutrition platform, FitWithTech! We're excited to embark on a journey with you towards a healthier and more active lifestyle. Our project is dedicated to providing tailored workout routines and diet plans to help you achieve your fitness goals. Whether you're aiming to build muscle, lose weight, or enhance overall well-being, our platform is designed to meet your unique needs. Explore a diverse range of workout programs crafted by fitness experts, and discover nutrition plans that align with your dietary preferences and goals. We believe in the power of a balanced approach to fitness, combining effective exercises with nourishing nutrition to optimize your results. Join us in creating sustainable habits and transforming your health. Let's make fitness a fulfilling and enjoyable part of your daily life!")
     st.subheader("Group Members-:")
     st.write("1.Gurlal Singh")
     st.write("2.Khush Nagpal")
     st.write("3.Anshika Sardana")

def page_nutrition():
    st.title("Track your Calories")

# Create a list of food items with their calorie information
    food_calories = [
    "Aloo Ki Sabzi: Around 150-200 calories per 100g (cooked).",
    "Aloo Paratha: Approximately 200-300 calories per paratha, depending on size and ingredients.",
    "Arhar Dal: About 150-170 calories per 100g (cooked).",
    "Biryani: Typically ranges from 300 to 400 calories per 100g, depending on the type (vegetable, chicken, or mutton).",
    "Butter Chicken: About 350-400 calories per 100g (cooked), excluding rice or naan.",
    "Chana Daal: Around 160-180 calories per 100g (cooked).",
    "Chicken Biryani: Usually contains 300-400 calories per 100g, excluding side dishes.",
    "Chicken Curry: Approximately 200-250 calories per 100g (cooked).",
    "Chicken Egg Roll: Roughly 250-300 calories per roll, depending on ingredients.",
    "Chicken Soup: Approximately 70-100 calories per serving, depending on the recipe.",
    "Daal Chawal: About 150-200 calories per 100g (cooked), excluding any additional ingredients.",
    "Dal: Typically contains 150-170 calories per 100g (cooked).",
    "Dosa, plain: Approximately 100-150 calories per dosa.",
    "Egg Fried Rice: Roughly 250-300 calories per serving, depending on ingredients.",
    "Egg Omelette: About 90-120 calories per 100g (cooked).",
    "Fish Curry: Typically ranges from 150 to 250 calories per 100g (cooked).",
    "Khichdi: About 200-250 calories per 100g (cooked), excluding ghee or other additions.",
    "Moong Masoor Dal: Around 150-170 calories per 100g (cooked).",
    "Mutton Curry: Approximately 250-300 calories per 100g (cooked).",
    "Noodle Soup: Roughly 100-150 calories per serving, depending on the recipe.",
    "Omelet: About 90-120 calories per 100g (cooked).",
    "Rajma: Approximately 150-170 calories per 100g (cooked).",
    "Sabji (Mixed Vegetables): Around 60-80 calories per 100g (cooked).",
    "Sambar: Typically contains 100-150 calories per 100g (cooked).",
    "Samosa: Roughly 250-300 calories per piece.",
    "Sandwich: Approximately 250-350 calories per sandwich, depending on ingredients.",
    "Spring Roll: About 100-150 calories per roll, depending on ingredients.",
    "Taco: Typically contains 150-200 calories per taco, depending on the filling and shell.",
    "Tandoori Chicken: Roughly 150-200 calories per 100g (cooked).",
    "Tomato Vegetable Soup: Typically contains 50-100 calories per serving."
]

# Define the Streamlit app title and introduction
    st.title("Food Calorie Information")
    st.subheader("1.Meals and Dishes")

# Display the food calorie information in bullet points
    st.markdown("\n".join(["- " + item for item in food_calories]))


    nut_calories = [
    "Almonds: Approximately 160 calories",
    "Cashews: Approximately 157 calories",
    "Chia Seeds: Approximately 138 calories",
    "Hazelnuts: Approximately 178 calories",
    "Mixed Nuts (combination of different nuts): The calorie count will vary depending on the types of nuts in the mix. On average, it's around 170-190 calories per 1 ounce.",
    "Peanut Butter (smooth, unsweetened): Approximately 180-190 calories per 2 tablespoons (32 grams).",
    "Peanuts: Approximately 160-170 calories",
    "Pumpkin Seeds (also known as pepitas): Approximately 153 calories",
    "Safflower Seeds: Approximately 80-90 calories",
    "Sesame Seeds: Approximately 160-170 calories",
    "Sunflower Seeds: Approximately 160-170 calories",
    "Tigernuts: Approximately 120-130 calories",
    "Walnuts: Approximately 185 calories"
]

    st.subheader("2.Nuts and Seeds")

    st.write("\n".join(["- " + item for item in nut_calories]))

    ingredients = [
    "All-Purpose Flour: Approximately 102 calories",
    "Barley: Approximately 100 calories",
    "Barley Flour: Approximately 100 calories",
    "Bread Flour: Approximately 102 calories",
    "Brown Sugar: Approximately 106 calories",
    "Chocolate Syrup: Approximately 52 calories",
    "Cocoa Powder: Approximately 12 calories",
    "Coconut Flakes: Approximately 197 calories",
    "Corn Flour: Approximately 100 calories",
    "Egg White: Approximately 17 calories",
    "Boiled Egg White: Approximately 17 calories",
    "Egg Yolk (raw): Approximately 55 calories",
    "Flour: Approximately 102 calories",
    "Glucose: Approximately 49 calories",
    "Gluten: Approximately 52 calories",
    "Granulated Sugar: Approximately 49 calories",
    "Jaggery: Approximately 383 calories",
    "Millet Flour: Approximately 103 calories",
    "Molasses: Approximately 58 calories",
    "Oat Bran: Approximately 83 calories",
    "Oats: Approximately 104 calories",
    "Powdered Sugar: Approximately 120 calories",
    "Quinoa (dry): Approximately 104 calories",
    "Sesame Flour: Approximately 157 calories",
    "Shredded Coconut: Approximately 187 calories",
    "Baking Soda: Negligible calories (virtually zero)",
    "Soy Flour: Approximately 98 calories",
    "Sugar: Approximately 49 calories",
    "Sunflower Seed Flour: Approximately 159 calories"
]

    st.write("\n".join(["- " + item for item in ingredients]))


def page_calories2():   
    st.title("How much Calories?")

# Define the Streamlit app title and introduction
    st.subheader("Daily Calorie Intake Calculator")
    st.write("This calculator estimates your daily calorie intake based on your age, gender, weight, height, and activity level.")

    # Input fields for user information
    age = st.number_input("Age (years)", 1, 120, 25)
    gender = st.radio("Gender", ("Male", "Female"))
    weight = st.number_input("Weight (kg)", 1.0, 500.0, 70.0)
    height = st.number_input("Height (cm)", 1, 300, 170)
    activity_level = st.selectbox(
        "Activity Level",
        ("Sedentary (little or no exercise)", "Lightly active (light exercise/sports 1-3 days/week)", "Moderately active (moderate exercise/sports 3-5 days/week)", "Very active (hard exercise/sports 6-7 days a week)", "Super active (very hard exercise and physical job or 2x training)"))

    # Calculate BMR (Basal Metabolic Rate) using Mifflin-St Jeor equation
    if gender == "Male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    # Calculate TDEE (Total Daily Energy Expenditure) based on activity level
    activity_levels = {
        "Sedentary (little or no exercise)": 1.2,
        "Lightly active (light exercise/sports 1-3 days/week)": 1.375,
        "Moderately active (moderate exercise/sports 3-5 days/week)": 1.55,
        "Very active (hard exercise/sports 6-7 days a week)": 1.725,
        "Super active (very hard exercise and physical job or 2x training)": 1.9
    }
    tdee = bmr * activity_levels[activity_level]

    # Display the calculated daily calorie intake
    st.write("Your estimated daily calorie intake is approximately:", int(tdee), "calories")




    

def page_workout():
    st.title("Workout")
    st.subheader("Welcome to the Workout Page!")
    if st.button("Tricep"):
        st.subheader("1.Seated Barbell Overhead tricep extension")
        st.write("1. BE careful getting the bar into place overhead. Push your elbows forward while keeping your elbows tucked in .")
        st.write("2.Loook for what feels like a strecth in your triceps . Extend your elbows until your firsts are pointed at the cilings.")
        st.video("C:/Users/dell/Downloads/t1.mp4")

        st.subheader("2.Barbell Overhead Press")
        st.write("1.Take a roughly shoulder width grip.There should be a straight line from your elbow to fist.")
        st.write("2.Pull your chin back and press the weight toward the ceiling by extending at the elbow joint and flexing at the shoulder joint.")
        st.write("3.Press untill your elbows are extended and push your head forward slightly.")
        st.write("4.Return to the start position with control.Pulling your chin back to allow the bar to press your face safely.")
        st.video("C:/Users/dell/Downloads/watermarked_preview (1).mp4")

        st.subheader("3.Barbell Skullcrusher")
        st.write("1Take a shoulder with a width grip . BReak at the elbows . Try to kepp your elbows tucked in. Don't let them flare out.")
        st.write("2.Stop the bar a few inches from ypur forehead and extend your elbows back up.")
        st.video("C:/Users/dell/Downloads/t3.mp4")

        st.subheader("4.Cable rope pushdown ")
        st.write("1.The cable should be set all the way at the top of the machine.")
        st.write("2.make sure to keep your upper arm glued at your side . Extend your elbows unti you feel your triceps contact .")
        st.video("C:/Users/dell/Downloads/t1.mp4")

        st.subheader("5.Diamond Push up")
        st.write("1.Position your index fingers and thumbs so they are touching, forming a diamond shape.")
        st.write("2 Use a standard push up position.")
        st.write("3.Lower your chest towards your handskeep your elbows close to your body")
        st.write("4 Stop just before your chest touches the floor, then push back up to the starting position.")
        st.video("C:/Users/dell/Downloads/01991201.mp4")


        st.subheader("6.Bench Dips ")
        st.write("1.Grip the edge of the bench with your hands, Keep your feet together and legs straight.")
        st.write("2.Lower your body straight down.")
        st.write("3.Slowly press back up to the starting point.")
        st.write("4  TIP: Make this harder by raising your feet off the floor and adding weight.")
        st.video("C:/Users/dell/Downloads/26971201.mp4")

        st.subheader("7.Cable triceps Kickback")
        st.write("1.Use a handle attachment. The cable should be set to hip height.")
        st.write("2.Hinge forward. Make sure to keep your upper arm glued at your side. Extend your elbows until you feel your triceps.")
        st.video("C:/Users/dell/Downloads/10681201.mp4")

        st.subheader("8.Cable Bar Reverse Grip Pushdown")
        st.write("1.Use the bar attachment. The cable should be set all the way at the top of the machine. Grab the bar with n overhand grip.")
        st.write("2.Make sure to keep your upper arm glued at your side. Extend your elbows until you feel your triceps contract.")
        st.video("C:/Users/dell/Downloads/16061201.mp4")
    
    if st.button("Biceps"):
            st.subheader("1. Biceps curls")
            st.write("Keep your elbows close to your torso at all times, and maintain your upper arms stationary as you curl the weights while contracting your biceps..")
            st.write("2 Continue to raise the barbell until your biceps are fully contracted and the bar is at shoulder level. Hold the contracted position for a brief pause as you squeeze your biceps.")
            st.write("3.Slowly begin to bring the barbell back to original position as your breathe in.Repeat this movement for the recommended amount of repetitions.")
            st.video("C:/Users/dell/Downloads/41521201.mp4")


            st.subheader("2. Dumble Hammer Curls")
            st.write("1.Keep your upper arms stationary, exhale and curl the weights while contracting your biceps. Continue to raise the weights until your biceps are fully contracted and the dumbbells are at shoulder level. Hold the contracted position for a brief pause as you squeeze your biceps.")
            st.write("2.Then, inhale and slowly begin to lower the dumbbells back to the starting position.")
            st.write("3.Repeat the process for the recommended amount of repetitions.")
            st.write("4.Ensure to keep your elbows close to your torso at all times and do not use your back or shoulders to lift the weights; your biceps should do all the work.")
            st.video("C:/Users/dell/Downloads/watermarked_preview (2).mp4")

            st.subheader("4. Preacher Curl")
            st.write("Pick up the barbell or dumbbells with an underhand grip, ensuring your hands are shoulder-width apart")
            st.write("2.Slowly curl the weight up, keeping your upper arms and elbows stationary on the pad, until your biceps are fully contracted and at shoulder level.")
            st.write("3.Hold the position for a second and squeeze your biceps at the top of the movement.Gradually lower the weight back to the starting position, maintaining control and resisting the pull of gravity. Repeat the exercise for the desired number of repetitions.")
            st.video("C:/Users/dell/Downloads/23851201.mp4")

            st.subheader("3.Dumbbell Incline Curl.")
            st.write("1.With your palms facing forward, curl the weights while contracting your biceps. Keep the upper arms stationary, only moving your forearms.")
            st.write("2.Continue to raise the weights until your biceps are fully contracted and the dumbbells are at shoulder level. Hold the contracted position for a brief moment as you squeeze your biceps.")
            st.write("3.Slowly begin to lower the dumbbells back to the starting position in a controlled manner.")
            st.write("4.Repeat the movement for the recommended amount of repetitions.")
            st.video("C:/Users/dell/Downloads/03151201.mp4")

            st.subheader("5.Dumbbell Prone Incline Curl.")
            st.write("1.Keep your elbows close to your torso and your back firmly against the bench.")
            st.write("2.Slowly curl the weights while keeping the upper arms stationary, continue to curl the weights until your biceps are fully contracted and the dumbbells are at shoulder level.")
            st.write("3.Hold the contracted position for a brief moment as you squeeze your biceps.Gradually lower the dumbbells back to the starting position, ensuring to keep your movements controlled and fluid throughout the exercise.")
            st.video("C:/Users/dell/Downloads/watermarked_preview (3).mp4")

            st.subheader("6.Concentration Curl.")
            st.write("1.Rest your right elbow on the inside of your right thigh, making sure your arm is fully extended and the palm of your hand is facing forward")
            st.write("2.Slowly curl the dumbbell up towards your chest, keeping your upper arm and elbow stationary on your thigh, only moving your forearm.")
            st.write("3.Pause for a moment at the top of the curl, contracting your bicep muscle.Slowly lower the dumbbell back down to the starting position, and repeat the movement for the desired number of repetitions before switching to your left arm.")
            st.video("C:/Users/dell/Downloads/02971201.mp4")

    if st.button("Chest"):
                st.subheader("1 Bench Press.")
                st.write("1.Grip the barbell with your hands slightly wider than shoulder-width apart, palms facing your feet, and lift it off the rack, holding it straight over your chest with your arms fully extended.")
                st.write("2.Slowly lower the barbell down to your chest while keeping your elbows at a 90-degree angle.")
                st.write("3.Once the barbell touches your chest, push it back up to the starting position while keeping your back flat on the bench.")
                st.write("4.Repeat this process for the desired number of repetitions, always maintaining control of the barbell and ensuring your form is correct.")
                st.video("C:/Users/dell/Downloads/00471201.mp4")

                st.subheader("2 Inclince Bench Dumble Press.")
                st.write("1.Grab the barbell with a grip that is slightly wider than shoulder-width apart, and remove it from the rack, holding it straight over your chest with your arms fully extended.")
                st.write("2.Slowly lower the barbell to your upper chest, ensuring that you keep your elbows at a 90-degree angle and your wrists straigth")
                st.write("3.Once the barbell has touched your chest, push it back up to the starting position, fully extending your arms but not locking your elbows.")
                st.write("4.Repeat this process for the desired number of repetitions, ensuring to maintain control of the barbell and your form throughout the exercise.")
                st.video("C:/Users/dell/Downloads/watermarked_preview (4).mp4")

                st.subheader("3 Decline Bench Press.")
                st.write("1.Lie down on the bench and reach up to grab the barbell with a grip slightly wider than shoulder width, ensuring your hands are evenly placed")
                st.write("2.Lift the barbell off the rack and hold it straight over your chest with your arms fully extended.")
                st.write("3.Gradually lower the barbell to your lower chest, keeping your elbows at a 90-degree angle and ensuring the barbell does not bounce off your chest.")
                st.write("4.Push the barbell back up to the starting position, fully extending your arms but not locking your elbows, and repeat for the desired number of repetitions.")
                st.video("C:/Users/dell/Downloads/03011201.mp4")

                st.subheader("4. Lever Seated Fly")
                st.write("1.With a slight bend in your elbows, start to bring the handles together in front of you in a smooth and controlled motion, focusing on squeezing your chest muscles.")
                st.write("2.Continue the motion until your hands meet in the middle, directly in front of your chest.")
                st.write("3.Hold the position for a second, ensuring you are fully contracting your chest muscles.")
                st.write("4.Slowly return the handles back to the starting position, allowing your chest muscles to stretch out, and repeat the exercise for the desired number of repetitions.")
                st.video("C:/Users/dell/Downloads/22551201.mp4")

                st.subheader("4.  Chest Dip")
                st.write("1.Lean your body forward to put emphasis on the chest muscles and bend your knees, crossing your ankles behind you to maintain balance.")
                st.write("2.Slowly lower your body by bending your elbows until you reach a point where your elbows are at a 90-degree angle and your chest is level with the bars")
                st.write("3.Pause for a moment at the bottom of the movement, then push yourself back up to the starting position, extending your arms fully but without locking your elbows")
                st.write("4.Repeat this process for the desired number of repetitions, ensuring to keep your body leaned forward throughout the exercise to maintain focus on the chest muscles.")
                st.video("C:/Users/dell/Downloads/35991201.mp4")

                st.subheader("5.Dumble Fly")
                st.write("1.Hold the dumbbells directly above your chest, with your palms facing each other and elbows slightly bent.")
                st.write("2.Slowly lower the dumbbells out to your sides in a wide arc, keeping the slight bend in your elbows, until you feel a stretch in your chest.")
                st.write("3.From this position, use your chest muscles to lift the dumbbells back up to the starting position, following the same wide arc.Repeat this movement for the desired number of repetitions, ensuring to keep your movements slow and controlled throughout the exercise.")
                st.video("C:/Users/dell/Downloads/12771201.mp4")


                st.subheader("6.Cable Low Fly")
                st.write("1.Stand in the middle of the cable machine, grab a handle in each hand, and step forward to create tension on the cables, keeping your feet shoulder-width apart.")
                st.write("2.Bend slightly at your knees and lean forward a bit at your waist, keeping your back straight")
                st.write("3.With your elbows slightly bent, lift your arms out to the sides and up until they are at chest level, forming a wide arc, and squeeze your chest muscles at the top of the movement.")
                st.write("4.Slowly lower your arms back down to the starting position, maintaining the slight bend in your elbows, and repeat the movement for your desired number of repetitions")
                st.video("C:/Users/dell/Downloads/01711201.mp4")


                st.subheader("7. Pullover")
                st.write("1.Hold a dumbbell with both hands above your chest, your arms should be fully extended and your palms should be facing up")
                st.write("2.Slowly lower the dumbbell back over your head while keeping your arms straight, until they are about parallel with the floor.")
                st.write("3.Hold this position for a moment to feel the stretch in your chest and lats.Then, use your chest and lats to pull the dumbbell back over your chest, returning to the starting position.")
                st.video("C:/Users/dell/Downloads/12841201.mp4")

    if st.button("Back"):
            st.subheader("2.Bar Lateral Pulldown")
            st.write("1.Sit down on the machine and grasp the bar with a wide grip, palms facing forward.")
            st.write("2.Pull the bar down towards your upper chest while keeping your back straight and squeezing your shoulder blades together.")
            st.write("3.Hold the position for a moment, then slowly return the bar back to the starting position, allowing your arms to fully extend.")
            st.write("4.Repeat this action for your desired number of repetitions")
            st.video("C:/Users/dell/Downloads/10471201.mp4")

            st.subheader("3.Dumbbell One Arm Bent-over Row")
            st.write("1.Bend your knees slightly and lean forward from your waist until your torso is almost parallel to the floor, making sure to keep your back straight")
            st.write("2.Hold onto the bench with your free hand for support, and let the hand holding the dumbbell hang down from your shoulder.")
            st.write("3.Pull the dumbbell up towards your waist, keeping your elbow close to your body and squeezing your shoulder blades together at the top of the movement.")
            st.write("4.Lower the dumbbell back down in a controlled manner to the starting position, and repeat the exercise for your desired number of reps before switching to the other arm")
            st.image("C:/Users/dell/Downloads/47301301-Dumbbell-Bent-over-Single-Arm-Row-(VERSION-2)_Back_720_small.png")

            st.subheader("4.Straight Back Seated Row")
            st.write("1.Grasp the handles with an overhand grip and sit upright, keeping your back straight and shoulders down.")
            st.write("2.Pull the handles towards your torso while keeping your elbows close to your body and squeezing your shoulder blades together.")
            st.write("3.Pause for a moment when the handles are close to your abdomen, then slowly extend your arms back to the starting position.")
            st.write("4.Repeat this motion for the desired number of repetitions, ensuring to maintain a straight back and controlled movements throughout the exercise.")
            st.video("C:/Users/dell/Downloads/02391201.mp4")

            st.subheader("5.Lever Lying T-Bar Row")
            st.write("1.Grasp the handles of the lever with an overhand grip, your hands should be wider than shoulder-width apart.")
            st.write("2.Pull the lever up towards your chest while keeping your elbows close to your body and squeeze your shoulder blades together at the top of the movement.")
            st.write("3.Hold for a moment at the top of the movement, then slowly lower the lever back to the starting position, ensuring to maintain control throughout the movement")
            st.write("4.Repeat the exercise for the desired number of repetitions, ensuring to maintain proper form throughout each repetition.")
            st.video("C:/Users/dell/Downloads/11941201.mp4")

            st.subheader("6.Barbell Bent Over Row")
            st.write("1.Bend your knees slightly and hinge at your waist, keeping your back straight and nearly parallel to the floor.")
            st.write("2.Pull the barbell towards your chest, keeping your elbows tucked in and squeezing your shoulder blades together at the top of the movement.")
            st.write("3.Slowly lower the barbell back to the starting position, fully extending your arms and stretching your lats.")
            st.write("4.Repeat this motion for your desired number of repetitions, ensuring to maintain a strong, stable posture throughout the exercise.")
            st.video("C:/Users/dell/Downloads/13441201.mp4")

            st.subheader("8.Cable Standing Lat Pushdown")
            st.write("1.Grasp the bar with an overhand grip, palms facing down and hands shoulder-width apart.")
            st.write("2.Start by pulling the bar down to your thighs while keeping your arms straight, your back upright and your shoulders down.")
            st.write("3.Pause for a moment at the bottom of the movement, focusing on squeezing your lat muscles.")
            st.write("4.Slowly return the bar back to the starting position, letting your lats stretch, and repeat the exercise for the desired number of repetitions.")
            st.video("C:/Users/dell/Downloads/12291201.mp4")

            st.subheader("10.Cable Seated Row with V bar")
            st.write("1.Grasp the V bar handles with both hands, palms facing each other, and lean back slightly while keeping your back straight.")
            st.write("2.Pull the V bar towards your waist while keeping your torso stationary, focusing on squeezing your back muscles and maintaining your posture.")
            st.write("3.Hold the contracted position for a moment, ensuring your muscles are fully engaged.")
            st.write("4.Slowly return the V bar to the starting position, allowing your arms to fully extend and your back muscles to stretch.")
            st.video("C:/Users/dell/Downloads/26611201.mp4")

            st.subheader("11. 45 degree hyperextension")
            st.write("1.Keep your body straight and bend at your waist while keeping your back flat, continue to lower your torso until you feel a mild stretch on the hamstrings.")
            st.write("2.Begin to raise your torso by extending through the hips with your back still kept straight, continue this movement until your body is in line with your legs")
            st.write("3.Hold this position for a few seconds, focusing on squeezing your glutes and hamstrings at the top of the movement.")
            st.write("4.Slowly lower your body back to the starting position, repeating the movement for the desired amount of repetitions.")
            st.video("C:/Users/dell/Downloads/08771201.mp4")

    if st.button("Legs"):
           
            st.subheader("1.Body wieght squat")
            st.write("1.Slowly bend your knees and lower your body as if you're about to sit on a chair, keeping your chest upright and your knees over your toes.")
            st.write("2.Continue lowering yourself until your thighs are parallel or almost parallel to the floor, this is the squat position.")
            st.write("3.Pause for a moment in the squat position, then push through your heels to rise back up to the starting position.Repeat this movement for the desired number of repetitions while maintaining proper form")
            st.video("C:/Users/dell/Downloads/08221201.mp4")

            st.subheader("2.Lever Leg Extension")
            st.write("1.Sit down on the machine and grasp the handles on either side of the machine to stabilize your upper body.")
            st.write("2.Slowly extend your legs, pushing against the pad, until they are fully straightened but not locked at the knee.")
            st.write("3.Hold this position for a moment, feeling the tension in your quadriceps.")
            st.write("4.Gradually lower your legs back to the starting position, making sure to control the movement rather than letting the weights drop quickly.")
            st.video("C:/Users/dell/Downloads/05851201.mp4")

            st.subheader("3.Lever Lying Leg Curl")
            st.write("1.Keep your torso flat on the bench as you fully extend your legs and grasp the side handles of the machine for stability.")
            st.write("2.Exhale and slowly curl your legs up as far as possible without lifting your upper legs from the pad. Your back should remain straight and stationary at all times.")
            st.write("3.Hold the contracted position for a moment as you squeeze your hamstrings.")
            st.write("4.Slowly bring your legs back to the initial position as you inhale, ensuring a controlled movement. This completes one repetition.")
            st.video("C:/Users/dell/Downloads/22231201.mp4")

            st.subheader("4.Sled 45° Leg Press")
            st.write("1.Place your feet shoulder-width apart on the platform, ensuring your toes are not hanging off the edge but are fully supported.")
            st.write("2.With your hands, grab the handles of the machine for stability, then press the weight up by fully extending your legs, making sure not to lock your knees at the top of the movement.")
            st.write("3.Slowly lower the weight by bending your knees until they form a 90-degree angle, keeping your feet flat on the platform at all times.")
            st.write("4.Push the weight back up to the starting position using your heels, not your toes, repeating the process for the desired number of repetitions.")
            st.video("C:/Users/dell/Downloads/36161201.mp4")

            st.subheader("5.Goblet Squat")
            st.write("1.Engage your core and keep your chest up, then start to lower your body into a squat position by bending your knees and pushing your hips back")
            st.write("2.Continue lowering yourself until your hips are below your knees, making sure your elbows are inside your knees at the bottom of the squat")
            st.write("3.Pause for a moment at the bottom of the squat, then push through your heels to stand back up to the starting position.")
            st.write("4.Repeat this movement for the desired number of repetitions, making sure to maintain proper form throughout the exercise")
            st.video("C:/Users/dell/Downloads/17601201.mp4")

            st.subheader("6..Lunge")
            st.write("1.Take a big step forward with your right foot while keeping your left foot in place.")
            st.write("2.Slowly lower your body until your front knee is bent at a 90-degree angle, ensuring your knee is directly above your ankle.")
            st.write("3.Keep your weight in your heels as you push back up to the starting position.")
            st.write("4.Repeat the same steps with your left foot stepping forward, and continue to alternate legs for the duration of your workout.")
            st.video("C:/Users/dell/Downloads/14601201.mp4")

            st.subheader("8.Hip Thrust")
            st.write("1.Place a barbell or weight across your hips, holding it in place with your hands.")
            st.write("2.Push through your heels to lift your hips towards the ceiling, ensuring that your body forms a straight line from your shoulders to your knees at the top of the movement.")
            st.write("3.Hold this position for a moment, then slowly lower your hips back down to the starting position.")
            st.write("4.Repeat this movement for the desired number of repetitions, ensuring that you keep your core engaged throughout the exercise to protect your lower back.")
            st.video("C:/Users/dell/Downloads/10601201.mp4")

    if st.button("Shoulders"):
        st.subheader("1.Cable Low Single Arm Lateral Raise")
        st.write("1.Use a handle attachment with the cable set all the way to the bottom of the machine.")
        st.write("2.You should vertically abduct at the shoulder raising your arm straight out to the side.")
        st.write("3.Raise until your arm is parallel with the ground and then back to the starting position.")
        st.video("C:/Users/dell/Downloads/01921201.mp4")

        st.subheader("2.Barbell Upright Row")
        st.write("1.Take a double overhand roughly shoulder width grip.")
        st.write("2.Pull your elbows straight up the ceiling.Aim to get the bar to chin level or slightly higher.")
        st.video("C:/Users/dell/Downloads/watermarked_preview (5).mp4")

        st.subheader("3.Dumbbell Front Raise")
        st.write("1.Grab two dumbbells while standing upright with the dumbbells at your side.")
        st.write("2.Raise the two dumbbells with your elbows being fully extended until the dumbbells are eye level.")
        st.write("3.Lower the weights in a controlled manner to the starting position and repeat.")
        st.video("C:/Users/dell/Downloads/watermarked_preview (6).mp4")

        st.subheader("4.Band pull apart")
        st.write("1.Grab the band with a shoulder width gripPoint your arms straight in front of you.")
        st.write("2.Retract your shoulder blades and shoulder joint until the band taps your chest.")
        st.video("C:/Users/dell/Downloads/09321201.mp4")

        st.subheader("5.Elevated Pike Press.")
        st.write("1.Use a bench or an object to elevate your feet.")
        st.write("2.Lower your head towards the floor by bending your elbows.")
        st.write("3.Push through your hands and return to the starting pike position.")
        st.write("4.Repeat.")
        st.image("C:/Users/dell/Downloads/image_iphone")

        st.subheader("6.Dumbbell Shrug")
        st.write("1.Stand Straight, palms facing your body, back straight.")
        st.write("2.Elevate your shoulders and hold the contracted position at the apex of the motion.")
        st.write("3.Slowly lower your shoulders back to starting position.")
        st.video("C:/Users/dell/Downloads/25961201.mp4")

        st.subheader("7.Barbell Upright Row")
        st.write("1.Take a double overhand roughly shoulder width grip.")
        st.write("2.Pull your elbows straight up the ceiling. Aim to get the bar to chin level or slightly higher.")
        st.video("C:/Users/dell/Downloads/watermarked_preview (7).mp4")

        st.subheader("8.Smith Machine Standing Shrugs")
        st.write("1.Place the bar on a lower rung so that when gripped your arms are fully extended and your back is straight.")
        st.write("2.Grip at shoulder width, raise the bar with your shoulders and pause at the contracted position.")
        st.write("3.Slowly lower the bar back to starting position.")
        st.video("C:/Users/dell/Downloads/07671201.mp4")


    

def page_bmi():
    def calculate_bmi(height, weight):
            if height <= 0 or weight <= 0:
                return 0
            bmi = weight / (height / 100) ** 2
            return bmi

    st.title("BMI CALCULATOR")
    height = st.number_input("Enter your height (in cm)", min_value=0)
    weight = st.number_input("Enter your weight (in kg)", min_value=0)

    if st.button("Calculate BMI"):
            bmi = calculate_bmi(height, weight)
            st.write(f"Your BMI is: {bmi:.2f}")

            # Interpret the BMI
            if bmi < 18.5:
                st.write("You are underweight.")
            elif 18.5 <= bmi < 24.9:
                st.write("You have a normal weight.")
            elif 25 <= bmi < 29.9:
                st.write("You are overweight.")
            else:
                st.write("You are obese.")

    st.markdown("BMI Categories:")
    st.markdown(" - Underweight: < 18.5")
    st.markdown(" - Normal Weight: 18.5 - 24.9")
    st.markdown(" - Overweight: 25 - 29.9")
    st.markdown(" - Obese: 30 or greater")
    
def page_yoga():
    st.title("Yoga Asanas")
    st.write("Yoga offers a multitude of physical, mental, and emotional benefits that contribute to overall well-being. Physically, it enhances flexibility, strength, and balance, making it an excellent exercise for improving posture and reducing the risk of injury. Moreover, yoga helps to manage stress by promoting relaxation and mindfulness through deep breathing and meditation techniques. It also supports mental clarity, focus, and a sense of inner peace. Regular practice can improve sleep quality, boost immune function, and even help manage chronic conditions like hypertension and anxiety. Yoga is a holistic approach to self-care that fosters a harmonious connection between the body, mind, and spirit, ultimately promoting a healthier and more balanced life.")
    st.write("Here are some Yoga Asanas which will help you in becoming fit-:")

    st.subheader("1.Cobra Yoga Pose")
    st.write("1.Press your palms into the mat, slowly lift your head, chest, and shoulders off the ground by straightening your arms, keep your lower body and hips on the ground.")
    st.write("2.Draw your shoulders back and down away from your ears to open up your chest.")
    st.write("3.Hold this pose for 15-30 seconds, remembering to breathe deeply and evenly.")
    st.write("4.To release, slowly lower your chest, shoulders, and head back to the mat, and rest your head to one side.")
    st.video("C:/Users/dell/Downloads/11.mp4")

    st.subheader("2.Butterfly Yoga Pose")
    st.write("1.Bend your knees, bring the soles of your feet together, and draw your heels as close to your body as you can, forming a diamond shape with your legs.")
    st.write("2.Hold onto your feet or ankles, keeping your elbows slightly bent and directed towards your knees..")
    st.write("3.Inhale deeply, and as you exhale, press your knees down towards the floor, trying to make them touch the ground; this will stretch your inner thighs and hips..")
    st.write("4.Hold this pose for 3-5 breaths, or as long as comfortable, then gently release your legs and return to the starting position..")
    st.video("C:/Users/dell/Downloads/14941201 (1).mp4")

    st.subheader("3.Wheel Pose Yoga Pose")
    st.write("1.Press down into your palms and lift your head, shoulders, and hips off the floor. Keep your thighs and feet parallel as you lift.")
    st.write("2.Push your chest towards the wall behind you and straighten your arms and legs as much as possible. Your body should be in a kind of semi-circle or 'wheel' shape.")
    st.write("3.Hold the pose for a few breaths, maintaining even pressure through your hands and feet.")
    st.write("4.To exit the pose, bend your elbows and knees and slowly lower your head, shoulders, and hips back to the floor.")
    st.image("https://apilyfta.com/static/GymvisualPNG/14931101-Wheel-Pose-Yoga-Pose__small.png")


    st.subheader("4.Locust Yoga Pose")
    st.write("1.Inhale and lift your head, upper body, arms, and legs off the floor. Your body should be resting on your lower ribs, belly, and front pelvis.")
    st.write("2.Stretch your arms back towards your feet and try to lift your thighs higher off the floor.")
    st.write("3.Hold this pose for 30 seconds to one minute, remembering to breathe evenly throughout.")
    st.write("4.Exhale as you lower your body back to the floor, rest for a few breaths, and repeat the pose if desired.")
    st.image("https://apilyfta.com/static/GymvisualPNG/14841101-Locust-Yoga-Pose-(Iron-Man-Pose)_Back_small.png")


    st.subheader("5.Plow Yoga Pose")
    st.write("1.Inhale and use your abdominal muscles to lift your legs and hips off the floor, bringing your torso perpendicular to the floor.")
    st.write("2.Slowly exhale and continue to lift your legs over your head, bending at the waist, lifting your back and buttocks until your toes touch the floor behind your head. Keep your legs straight")
    st.write("3.Keep your hands on your lower back for support, or you can clasp them together and stretch them out behind you on the floor.")
    st.write("4.Hold the pose for 5 to 10 breaths, then slowly roll your spine back down onto the floor, keeping your legs raised towards the ceiling, then lower them down as you exhale.")
    st.image("https://apilyfta.com/static/GymvisualPNG/14851101-Plow-Yoga-Pose_Waist_small.png")

    st.subheader("6.Supine Spinal Twist Yoga Pose")
    st.write("1.Slowly, bend your right knee and bring it towards your chest, then gently guide it across your body using your left hand, aiming to place your right knee on the left side of your body.")
    st.write("2.Extend your right arm out to the right side, keeping it in line with your shoulder, and turn your head to look towards your right hand.")
    st.write("3.Hold this position for a few breaths, feeling the stretch along your spine and in your lower back.")
    st.write("4.Gently return to the starting position and repeat the same steps on the opposite side.")
    st.video("C:/Users/dell/Downloads/14911201 (2).mp4")


    st.subheader("7.Bow Yoga Pose")
    st.write("1.Bend your knees and bring your heels as close as you can to your buttocks, then reach back with your hands and grasp your ankles.")
    st.write("2.Inhale deeply, and as you exhale, lift your chest and thighs off the floor by pulling your ankles up and back, keeping your body tight like a bow.")
    st.write("3.Hold this pose for 15-20 seconds, remembering to breathe evenly and deeply.")
    st.write("4.To release the pose, gently lower your chest and thighs back to the floor, release your ankles, and relax with your arms at your sides.")
    st.image("https://apilyfta.com/static/GymvisualPNG/14811101-Bow-Yoga-Pose_Back_Hips_Thighs_small.png")

    st.subheader("8.Legs-Up The Wall Yoga Pose")
    st.write("1.Carefully, lie on your back while simultaneously swinging your legs up onto the wall.")
    st.write("2.Adjust your body so that your buttocks are as close to the wall as possible and your back and head are resting comfortably on the floor.")
    st.write("3.Place your arms out to your sides with palms facing up, relax your body and breathe deeply, keeping your legs relatively straight")
    st.write("4.Hold this pose for 5-15 minutes, then gently slide your legs down the wall, roll to your side and get up slowly.")
    st.image("https://apilyfta.com/static/GymvisualPNG/43811101-Legs-Up-The-Wall-Yoga-Pose_Stretching_small.png")

    st.subheader("9.Butterfly Yoga Pose")
    st.write("1.Bend your knees and bring the soles of your feet together, allowing your knees to drop out to the sides like a butterfly's wings")
    st.write("2.Hold onto your feet or ankles, keeping your back straight and your shoulders relaxed.")
    st.write("3. Gently press your knees down towards the floor using your elbows, but don't force them down.")
    st.write("4.Stay in this pose for 1-5 minutes, breathing deeply, and then gently release the pose by lifting your knees and extending your legs back in front of you.")
    st.video("C:/Users/dell/Downloads/45081201 (1).mp4")


    st.subheader("10.Full Lotus Yoga Pose")
    st.write("1.Bend your right knee and bring the ankle to the crease of your left hip with the sole of your foot facing upwards, this is the Half Lotus position.")
    st.write("2.Now, bend your left knee and carefully place your left ankle on top of the right thigh, bringing it towards the crease of your right hip.")
    st.write("3.Make sure that both your feet are facing upwards and your heels are close to your abdomen.")
    st.write("4.Make sure that both your feet are facing upwards and your heels are close to your abdomen.")
    st.image("https://apilyfta.com/static/GymvisualPNG/44061101-Tiger-Yoga-Pose_Stretching_small.png")

    st.subheader("11.Animal Resting Yoga Pose")
    st.write("1.Slowly lean forward, extending your arms in front of you and lowering your torso between your thighs.")
    st.write("2.Rest your forehead gently on the floor, keeping your arms extended or you can also bring them back alongside your body.")
    st.write("3.Breathe deeply and relax in this position for about 5 to 10 minutes, allowing your body to fully rest and rejuvenate.")
    st.write("4.To exit the pose, slowly lift your forehead off the floor, walk your hands back towards your knees, and return to the kneeling position.")
    st.image("https://apilyfta.com/static/GymvisualPNG/43651101-Animal-Resting-Yoga-Pose_Stretching_small.png")

    st.subheader("12.Straight Angle Yoga Pose")
    st.write("1.Slowly raise your arms up towards the sky, keeping them straight and parallel to each other, palms facing each other.")
    st.write("2.As you inhale, lean your torso back slightly while keeping your hips forward, creating a straight angle with your body..")
    st.write("3.Hold this pose for a few breaths, focusing on keeping your body straight and your breathing steady.")
    st.write("4.To release the pose, exhale and slowly lower your arms back to your sides while straightening your torso.")
    st.image("https://apilyfta.com/static/GymvisualPNG/44021101-Straight-Angle-Yoga-Pose_Stretching_small.png")


    st.subheader("13.Cobra Yoga Pose")
    st.write("1.Place your palms on the floor under your shoulders and keep your elbows close to your body.")
    st.write("2.Inhale and slowly lift your chest off the floor by straightening your arms, while keeping your lower body in contact with the floor.")
    st.write("3.Keep your shoulders relaxed and away from your ears, and gaze slightly upwards or straight ahead.")
    st.write("4.Hold the pose for about 15 to 30 seconds, then exhale and slowly lower your body back to the floor.")
    st.video("C:/Users/dell/Downloads/42671201 (1).mp4")

    st.subheader("14.Prayer Squat Yoga Pose")
    st.write("1.Slowly lower your body into a squat position, bending your knees and pushing your hips back as though you are sitting in an imaginary chair.")
    st.write("2.Bring your palms together in a prayer position in front of your chest, keeping your elbows inside your knees.")
    st.write("3.Hold this position, keeping your spine straight and your chest lifted for as long as comfortable, focusing on your breath.")
    st.write("4.To release the pose, slowly straighten your legs and stand back up, lowering your arms to your sides.")
    st.image("https://apilyfta.com/static/GymvisualPNG/43871101-Prayer-Squat-Yoga-Pose_Stretching_small.png")

    st.subheader("15.Warrior II Yoga Pose")
    st.write("1.Turn your right foot out 90 degrees, so your toes are pointing to the top of the mat, and pivot your left foot slightly inwards about 45 degrees.")
    st.write("2.Raise your arms parallel to the floor, palms facing down, aligning them directly over your legs with your right arm pointing forward and left arm pointing back.")
    st.write("3.Bend your right knee, making sure it's directly over your right ankle, while keeping your left leg straight.")
    st.write("4.Hold this pose for about 30 seconds to a minute, keeping your gaze fixed over your right hand, then switch sides and repeat the process.")
    st.image("https://apilyfta.com/static/GymvisualPNG/44101101-Warrior-II-Yoga-Pose_Stretching_small.png")

    st.subheader("16.Crocodile Yoga Pose")
    st.write("1.Keeping your hands flat on the mat, slide them under your shoulders and press your upper body up, extending your spine as you lift your chest and head, similar to the Cobra pose but keep the elbows bent and close to your body.")
    st.write("2.Now, turn your head to the right and rest your left cheek on the mat. Your gaze should be towards your left hip.")
    st.write("3.Hold this pose for a few moments, breathing deeply and feeling the stretch in your back and neck.")
    st.write("4.Release the pose by slowly lowering your chest and head back down to the mat, then repeat the exercise with your head turned to the left and your right cheek on the mat.")
    st.image("https://apilyfta.com/static/GymvisualPNG/43721101-Crocodile-Yoga-Pose_Stretching_small.png")


    st.subheader("17.Tiger Yoga Pose")
    st.write("1.Inhale and lift your right leg up towards the ceiling, bending at the knee so the sole of your foot faces the sky.")
    st.write("2.Extend your left arm in front of you, parallel to the ground, while maintaining a steady balance.")
    st.write("3.Extend your left arm in front of you, parallel to the ground, while maintaining a steady balance.")
    st.write("4.Exhale and lower your arm and leg back to the tabletop position, and repeat the process with your left leg and right arm.")
    st.image("https://apilyfta.com/static/GymvisualPNG/44061101-Tiger-Yoga-Pose_Stretching_small.png")

    
pages = ["About this project", "Workout","Yoga Asanas","Track your Calories", "How much Calories?", "BMI"]
selected_page = st.sidebar.selectbox("Select a page", pages)


if selected_page == "About this project":
     page_home()
if selected_page == "Track your Calories":
    page_nutrition()
elif selected_page == "Workout":
    page_workout()
elif selected_page == "BMI":
    page_bmi()
if selected_page == 'How much Calories?':
    page_calories2()
if selected_page == 'Yoga Asanas':
     page_yoga()


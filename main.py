import tkinter as tk
from PIL import Image, ImageTk

class AdventureGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Escape Dracula's Castle: Designed and Created by Ronald A Zirk")
        self.geometry("1980x1024")
        self.configure(bg="black")
        self.configure(pady=5)
        # Initialize current stage
        self.current_stage = 0


        self.stages = [
            #0
            ("Rain pours over your black overcoat,like fine wiskey over ice.\n"
             "The wind howls like the dogs of hades them selves.\n"
             "The worst storm of the 1910's, the papers would later say.\n"
             "First day as a postman and this is how its going," "you think to yourself.\n"
             "Up in the distance, just off a short dirt path, you see a large house.\n" 
             "Some might even say a castle.\n"
             "Although from this distance in the storm it appears to be long abandoned.\n"
             "Knowing you've little time before the parcels in your pouch are damaged,\n"
             "you make your way to the mansion to wait out the encroaching storm . Do you:", "Take shelter in the house", "Quit and go home", "castle.png"),
            #1
            ("Out of breath, and soaked to the core, you swing open the large oak door.\n"
             "Slowly stepping a few paces into the room.\n"
             "You gaze around the dimly lit entrance way.\n"
             "On the back wall a large painting catches your eye.\n"
             "There is also a door with an oddly shaped symbol in the center of the door "
             "Do you:", "Investigate the portrait", "Investigate the door", "room1.4.png"),
            #2
            (
             "Straining to see in the dim light, your eyes race across the painting.\n"
             "As you study the painting... you realize somthing is'nt right....\n"
             "The eyes... It's like they are watching your every move.\n"
             "The lightening strikes outside again, and that's when you see it...\n "
             "The same man, shrouded in black mist, but recognizable still, standing beside the painting. \n"
             "Frozen in shock... eye's locked with his...\n"
             "A maniacal cackling erupts from what seems like all around you\n"
             "A voice ripples though your mind like a shockwave, speaking a language you have never heard before.\n"
             "Instantly the feeling of doom surrounds you, with what feels like a million eyes gazed fixed on you.\n"
             "As quickly as he appeared, the man vanishes... Do you:", "Run for the door leading outside", "Run to the strange door", "vampire3.png"),
            #3
            ("You scan over the strange symbols on the door.\n"
             "You notice that one of the symbols is glowing a faint red glow.\n"
             "Under the glowing symbol appears to be an outline of a handprint\n"
             "Do you:", "Place your hand over the handprint under the glowing symbol", "Attempt to kick the door open", "strangedoor.png"),
            #4
            ("You attempt to run to the open front door."
             "The cackling growing louder and louder in your ears!\n"
             "To your horror the door slams shut right as you reach it!\n Do you:", "Try and force the door open", "Run to the door with the strange symbol?", "exitdoor.png"),
            #5
            ("As you walk over to the red jewel. You can sense an immense power radiating out of it.\n"
             "The closer you get to the jewel, the louder the whispering in your ears becomes.\n"
             "You find yourself staring deeply into the jewel.\n"
             "Before you realize it, your hand is just inches from the jewel.\n"
             " Do you:", "Touch the red jewel", "resist the urge and go up the stairs", "jewel.png"),
            #6
            (" As you place your hand on the door. A strange voice whispers in your mind in a language you've never heard before\n"
             "A sense of dread fills your body as the door begins to dissolve into mist.\n"
             "The mist dissipates, revealing a beautiful crimson ballroom.\n"
             "In the center of the room there is a large red pulsating jewel, the likes you've never seen.\n"
             "On the opposite side of the room there is a large spiral stair case leading upwards\n"
             "Do you:","Walk over and investigate the jewel","Ascend the staircase","openstrangedoor.png"),
            #7
            ("You walk up the stairs and enter what appears to be a throne room.\n"
             "There is a large throne adorned in strange writings and symbols.\n"
             "There is also a small staircase in the far corner leading up.\n"
             "Do you:","Approach the throne ","Quickly make your way up the small staircase","throneroom.png"),
            #8
            ("You walk up the small stairway and find yourself in a high watch tower.\n"
             "There is a massive stain glass window overlooking the courtyard many stories below.\n"
             "As you look around the room,you are struck with overwhelming terror, as the door leading from the stairs slam shut behind you.\n"
             "To your horror, you see a black mist begin to form into a human shape.\n"
             "In the blink of an eye, the mist solidifies and in its place stands a terrifying figure.\n"
             "The figure smiles, reviling two huge fans.\n"
             "You realize you are trapped and only have two options.Fight or leap to your death.\n"
             "Do you:","Charge at the creature,engaging in a fight for survival.","Jump though the stain glass window,a quick death is preferable to whatever the creature has in store","tower.png"),

        ]

        self.outcomes = [
            #9
            ("Only those who are truly worthy will face the darkness.", "drac.png"),
            #10
            ("As you kick against the door, it immediately dissolves into mist.\n"
             "Staggering forward you find yourself in an endless dark void.\n"
             "You feel an icy chill race down your spine as a voice whispers in your mind.\n"
             "Welcome to my domain mortal,I will show you true darkness.\n"
             "Suddenly two sharp fangs peirce the side of your neck.\n"
			 "They feel like two molten hot daggers stabbing into you.\n"
             "Your life slowly drains away in the creatures embrace as you slip away into oblivion.","blackroom.png"),
			#11
			("You sprint to the front door in attempts to pry it open. \n"
             "You strain with all your might, your fingers feeling like they are about to break.\n"
             "In that moment an icy chill consumes you,freezing your body in place\n"
             "As it does you feel two sharp fangs peirce the side of your neck.\n"
			 "They feel like two molten hot daggers stabbing into you.\n"
			 "As your vision turns black you hear the man wisper in your mind.\n"
			 "---Good I was starting to hunger---\n"
			 "It all fades to black...\n", "drac.png"),
            #12
            ("You are instantly racked with unbearable pain.\n"
             "You collapse to your knees in agony.\n"
             "Maddening screams fill your ears as you force your eyes open.\n"
             "To your horror,you surrounded by grotesque creatures.\n"
             "The instant your eyes meet theirs,they descend upon you.\n"
             "The creatures show no mercy.\n"
             "Nothing remains but shreds of your ripped flesh.","demons.png"),
            #13
            ("As you approach the throne a searing pain rips though your mind.\n"
             "A force that feels like multiple sledge hammer blows slams onto your back forcing you to your knees.\n"
             "Instantly your head snaps forward by an unseen force, locking the rest of your body in place."
             "To your horror,on the throne now sits a large creature."
             "A voice whispers in your mind,the words feel like maggots crawling around your brain.\n"
             "Foolish mortal, you stand before darkness itself."
             "Ive been called many things over the millennia, but you would know me as...."
             "Dracula\n"
             "In that moment,your vision turns to black,and you hear the creature whisper in your mind.\n"
             "---Good I was starting to hunger---\n","dracthrone.png"),
			#14
			("In a desperate fury you charge at the creature, letting out a primal yell as you rush forward."
             "The creature's glowing red eyes meet yours and instantly you are completely frozen in place."
             "Pure terror floods over you as you struggle to move your totally paralyzed body. "
             "A voice whispers in your mind,the words feel like maggots crawling around your brain.\n"
             "Foolish mortal, you stand before darkness itself.\n"
             "Ive been called many things over the millennia, but you would know me as....\n"
             "Dracula\n"
             "In that moment,your vision turns to black,and you hear the creature whisper in your mind.\n"
             "---Good I was starting to hunger---\n"
             "It all fades to black...", "fight.png"),
            #15
            ("Having no other options, you sprint towards the stained glass window."
             "Throwing your body at the glass, it instantly shatters as you begin to plummet to the ground below."
             "You clench your eyes shut and accept your fate."
             "After a few moments, you realize you should have hit the ground already."
             "You slowly open your eyes and are stunned at what you see."
             "You find yourself lying on your back in front of a long abandoned shack."
             "How is this possible ? Your mind races to make sense of what just happened"
             "Was the creature even real and where did the castle go? "
             "As you sit up you discover theres a letter in your hand with a strange symbol on it."
             "Reading the address on the letter, you look up at the old shack,and see the address written beside the door frame"
             "You realize the addresses match.In confusion and disbelief you begin walking away from the shack."
             "However as you do, you take one last glance back at the old shack,and for just a split moment you could have sworn you saw a dark figure in the window."
             ,"oldhouse.png")

        ]

        self.next_stages = {
            0: (1, 9),   # Take shelter or quit
            1: (2, 3),   # look at door or picture
            2: (4, 3),   # run outside or run to strange door?
            3: (6, 10),   # touch glowing symbol, attempt to run though?
            4: (11, 3),   # front door choice
            5: (12, 7),  # touch or no
            6:(5,7),  # jewel or stairs
            7:(13,8), #sit on throne or not
            8:(14,15),#fight or jump
        }

        self.create_widgets()

    def create_widgets(self):
        self.story_label = tk.Label(self, text="Welcome to Dracula's Castle", font=("Helvetica", 10),wraplength=600)
        self.story_label.pack()
        self.story_label.config(height=10,width=100)
        self.image_label = tk.Label(self)

        self.image_label.pack(pady=10)

        self.option1_button = tk.Button(self, text="Option 1", command=lambda: self.next_stage(1))
        self.option2_button = tk.Button(self, text="Option 2", command=lambda: self.next_stage(2))

        self.option1_button.pack(pady=5)
        self.option2_button.pack(pady=5)

        self.update_story()

    def update_story(self):
        if self.current_stage < len(self.stages):
            self.story_label.config(text=self.stages[self.current_stage][0])
            self.option1_button.config(text=self.stages[self.current_stage][1])
            self.option2_button.config(text=self.stages[self.current_stage][2])
            image_path = self.stages[self.current_stage][3]
        else:
            outcome_index = self.current_stage - len(self.stages)
            self.story_label.config(text=self.outcomes[outcome_index][0])
            image_path = self.outcomes[outcome_index][1]
            self.option1_button.pack_forget()
            self.option2_button.pack_forget()

        self.display_image(image_path)

    def display_image(self, image_path):
        img = Image.open(image_path)
        img = img.resize((550, 400))
        img = ImageTk.PhotoImage(img)
        self.image_label.config(image=img)
        self.image_label.image = img

    def next_stage(self, choice):
        if self.current_stage in self.next_stages:
            self.current_stage = self.next_stages[self.current_stage][choice - 1]
        else:
            self.current_stage += 1

        self.update_story()

if __name__ == "__main__":
    app = AdventureGame()
    app.mainloop()
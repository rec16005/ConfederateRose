# Script.rpy
#transitions:
transform pop:
   yzoom 1.0
   linear 0.125 yzoom 1.025
   linear 0.125 yzoom 1.0
init:
    $ s = 0 # this is a variable for bob's affection points throughout your game
    $ suspicion_max = 3 # this variable should be set to bob's maximum affection points

    python:
    
        import math
        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)





init python:
 #   speaker = None
    speaking = None
    def while_speaking(name, speak_d, done_d, st, at):
        if speaking == name:
            return speak_d, .1
        else:
            return done_d, None
    curried_while_speaking = renpy.curry(while_speaking)
    def WhileSpeaking(name, speaking_d, done_d=Null()):
        return DynamicDisplayable(curried_while_speaking(name, speaking_d, done_d))
    def speaker_callback(name, event, **kwargs):
        global speaking
        if event == "show":
            speaking = name
            # if speaking=="Rose":
            #  renpy.sound.play("blip2.wav")
            # if speaking=="Rose":
            #  renpy.sound.play("blip.wav") 
        elif event == "slow_done":
            renpy.music.stop()
            speaking = None
        elif event == "Pause":
            renpy.music.stop()
            speaking = None 

        elif event == "end":
            #renpy.music.stop(1,False)
            renpy.music.stop()
            speaking== None
    speaker = renpy.curry(speaker_callback)   

define r = Character("Rose", color="#FE2E64",callback=speaker("Rose"),what_slow_cps=30)
define j = Character("June", color="#2E64FE")
define u = Character("????", color="#D8D8D8",callback=speaker("Rose"))
define ol = Character("Old Lady", color="#F5A9F2")
define olm = Character("Old Man", color="#F5A9F2")
define a = Character("Alarm")


    

#Backrounds
image bg arbol = im.Scale("arbol.png", 1280, 720)
image bg adentrocine = im.Scale("AdentroCine.png", 1280, 720)
image bg aerepuerto = im.Scale("Aereopuerto.png", 1280, 720)
image bg benchatnight = im.Scale("BenchAtNight.png", 1280, 720)
image bg biblioteca = im.Scale("Biblioteca.png", 1280, 720)
image bg cafe = im.Scale("Cafe.png", 1280, 720)
image bg calleinglesadia = im.Scale("CalleInglesaDia.png", 1280, 720)
image bg calleinglesanoche = im.Scale("CalleInglesaNoche.png", 1280, 720)
image bg carrosospechoso = im.Scale("CarroSospechoso.png", 1280, 720)
image bg centrouni = im.Scale("CentroYale.png", 1280, 720)
image bg cherrypath = im.Scale("CherryPath.png", 1280, 720)
image bg cuartodorm = im.Scale("CuartoDorm.png", 1280, 720)
image bg dentrocampus = im.Scale("DentroCampus.png", 1280, 720)
image bg edifapt = im.Scale("EdificioApt.png", 1280, 720)
image bg exteriorbnch = im.Scale("ExteriorBenchNight.png", 1280, 720)
image bg pared = im.Scale("Pared.png", 1280, 720)
image bg parquenoche = im.Scale("ParqueNoche.png", 1280, 720)
image bg pasillodorm = im.Scale("PasilloDorm.png", 1280, 720)
image bg portaly = im.Scale("PortalYale.png", 1280, 720)
image bg puente = im.Scale("Puente.png", 1280, 720)
image bg salidatren = im.Scale("SalidaTren.png", 1280, 720)
image bg salonclase = im.Scale("SalonClase.png", 1280, 720)
image bg ventisca = im.Scale("Ventisca.png", 1280, 720)
image bg ventisca2 = im.Scale("Ventisca2.png", 1280, 720)
image bg mall = im.Scale("Mall.png", 1280, 720)
image bg heladeria = im.Scale("Heladeria.png", 1280, 720)
image bg lobbycine = im.Scale("LobbyCine.png", 1280, 720)
image bg afueracine = im.Scale("AfueraCine.png", 1280, 720)
image bg pasajero = im.Scale("Pasajero.png", 1280, 720)
image bg universidad = im.Scale("Universidad.png", 1280, 720)
image bg cafeteria = im.Scale("Cafeteria.png", 1280, 720)
image bg black = im.Scale("Black.png", 1280, 720)
image bg final = im.Scale("main_menu.png", 1280, 720)


image rose = LiveComposite(
    (584,720),
    (0, 0), "rose[rose].png",
    (0, 0), "rose[rose].png",
    (0, 0), WhileSpeaking("Rose", ConditionSwitch( "(sadrose != 'sad')", "rose mouth normal", "(sadrose == 'sad')", "rose mouth night"), "rose[rose].png"),
    (0, 0), ConditionSwitch( "roseblush == 'blushing'", "images/speaking/blush.png", "roseblush == 'notblushing'", "images/speaking/blank.png"))


image nrose = LiveComposite(
    (584,720),
    (0, 0), "Nrose[nrose].png",
    (0, 0), "Nrose[nrose].png",
    (0, 0), WhileSpeaking("Rose", ConditionSwitch( "nrose != 'happy'", "rose mouth night", "nrose == 'happy'", "rose mouth normal"), "Nrose[nrose].png"),
    (0,0), ConditionSwitch( "roseblush == 'blushing'", "images/speaking/blush.png", "roseblush == 'notblushing'", "images/speaking/blank.png"))

image rose mouth normal:
    "images/speaking/Rosespk.png"
    pause .08
    "images/speaking/Rosespk2.png"
    pause .1
    "images/speaking/Rosespk3.png"
    pause .08
    "images/speaking/Rosespk4.png"
    pause .1
    "images/speaking/Rosespk5.png"
    pause .08
    "images/speaking/Rosespk6.png"
    pause .1
    "images/speaking/Rosespk7.png"
    pause .08
    "images/speaking/Rosespk8.png"
    pause .08
    repeat 

image rose mouth night:
    "images/speaking/Rosespk10.png"
    pause .08
    "images/speaking/Rosespk11.png"
    pause .1
    "images/speaking/Rosespk12.png"
    pause .08
    "images/speaking/Rosespk13.png"
    pause .1
    "images/speaking/Rosespk14.png"
    pause .08
    "images/speaking/Rosespk15.png"
    pause .1
    "images/speaking/Rosespk16.png"
    pause .08
    "images/speaking/Rosespk17.png"
    pause .08
    repeat 

label start:
    
    $ b = 0
    $ s = 0
    $ n = 0
    $ g = 0
    $ ans = 0
    
    scene bg ventisca2
    $ night = ""
    $ rose  = "happy"
    $ nrose = "mad"
    $ roseblush = "notblushing"
    $ sadrose='notsad'
    
    "The air was cold, June felt the snowflakes touch his skin, but he was so cold they didn’t even melt."
    "It was not his first time in England but he was amazed at the white snow that covered the streets."
    "June knew for fact that those flakes weren't natural and that amidst the peace they gave to him, they were silently deadly. Human time on earth was reaching its end."
    "Since the atmosphere became so polluted with carbon dioxide and other gases, humans can no longer reproduce normally. The new human generation was created."
    "On the verge of extinction, old scientists discovered a way to create humans on labs."
    "These humans are special, they are custom made. The skin color, the hair, the eyes, the personality, everything you desire on a child is possible, for a price."
    
    scene bg aerepuerto with fade
    "June walked towards the airport Exit. Absorbed in his thoughts."
    
    
    "When he finally got out of that mess, he jumped on those fancy new self-driving eco cars that the British implemented a few years ago. He paid his fee and selected where he wanted to go, for a moment, he was free."
    "The ride towards the university was very fast, he didn’t even notice anything because after a few blocks he was fast asleep."
    
    
    "He stepped out of the car, took his luggage and walked to the building’s entrance. There was a big wooden sign on the outer wall that read: “Agnes Arber Dormitory”. He proceeded to the reception where he registered with his foreign ID."
    "He went up the old, wooden and squeaky steps towards his room in the 6th floor{w=.3}.{w=.3}.{w=.3}. At the end of such hike, he was exhausted, so he just collapsed on his bed and closed his eyes for a moment, or so he thought."
    
    scene bg cuartodorm with fade
    "He suddenly felt like he was being watched from behind…"
    "He turned around just in time to see a shadow disappear by the door. He didn’t have the chance to look at it with detail. He was so scared that he locked the door and went to sleep."
    
    "*Day 1*"
    scene bg cuartodorm with fade
    "I wake up by mere coincidence, didn’t even set an alarm or anything. Weird, I thought I didn’t sleep at all but it seems fatigue kicked in at last."
    "I am all settled in, just finished unpacking the things that I had on my suitcase and placed them on the only drawer the little room had. Just beside the pink duvet of the bed."
    "I go to the bathroom and take a shower. I see a hair dryer hanging in it’s holder."
    j "Hm… it’s weird that my room has a hair dryer. That is some quality appliances for the price I pay for this room."
    
    scene bg pasillodorm with fade
    "Suddenly I hear someone knock on the door, and as I'm just getting out of the shower, just with a  towel on. I approach the door and proceed to open it."
    "There is an old lady at the other side, I'm kinda surprised but at the same time I'm just as embarrassed."
    ol "Just how indecent are women today! Cover yourself girl! I don’t care how flat chested you are, it is simply not right to open the door without a shirt!"
    "I'm confused."
    scene bg cuartodorm with fade
    "I close the door as fast as I can and grab the first shirt I find in my room and just place it in front of me."
    ol "Now, now. I’m just visiting my new tenant, it is not an inspection for now, just remember that a proper lady must be visible at all times!"
    "I'm still as confused as before."
    "With that the Old lady turns around and leaves my room. I check the clock. 6:45. I’m running late for my first class!. I brush my teeth hastily and run half dressed to the hall."
    "I’m paralyzed at my room’s entrance."
    "There is only girls at my floor not a single boy to be seen. I don’t know what to do so I just walk pass some sleepy looking girls and take the stairs to the first level." 
    scene bg pasillodorm with fade
    show rose chall with dissolve
    "While I'm at it, i glimpse at a white haired girl gazing at my direction fixedly, maybe I’ve been exposed?." 
    "She simply turns around and lets me escape the maelstrom."
    
    hide rose with fade
    scene bg universidad with fade #aun no esta esta madre
    "It takes a 15-minute walk to get to campus. It is an old looking building, it has a cliche looking main entrance with cherry trees on both sides, sadly it's winter so they do not have any leaves."
    
    scene bg salonclase with fade
    "I walk into class and proceed to take a sit on the last row, near the window because I like feeling the wind in  my skin."
    "Not even 5 minutes go by when a crowd of students flood the room and take their places."
    "For a moment, I’m frozen in time, the same girl from this morning is moving in my direction."
    "Panic."
    "She walks the distance there is from the door to my place and proceeds to take a sit just at my side. I don't know yet, but I think I just dodged a bullet."
    "Class is just as boring as expected, so I feel relieved when the bell rings. I proceed to stand up and walk towards the class exit, but someone stands in front of me and doesn't let me get to it."
    show rose with dissolve
    u "Hi I don’t believe I’ve introduced myself, I'm Rose, your neighbor. Pleased to meet you."
    j "Hi, my name is June, I moved in yesterday to your apartment complex and it looks like we are on the same… class."
    "I don’t even remember the name of the class we’d just recieved so I space out for a moment there, enough time for her to notice."
    $ rose = "happyclose"
    "She chuckles a little bit when I try to remember the name of the course."
    $ rose  = "happy"
    show rose  happy with dissolve
    r "You seem kinda lost, Are you alright?, Maybe I can walk with you back to the dormitories."
    j "Don't you think it will be weird?"
    $ rose  = "challenging"
    show rose  chall with dissolve
    r "What do you mean? We girls should protect each other backs."
    "I see now, I was mistaken as a girl and put in the girls dorm. A foolish mistake, but I can not back down now, I have to keep my facade."
    
    #Show bar
    
    "This is the suspicion bar, if it gets full, people will suspect that you are not a girl, try not to fill it if you wish to stay hidden."
    "You can find out your suspicion points under the 'Stats' tab down, try to keep it down or bad things will happen!"
    
    #Continue Dialogue
    "Well I don’t want  to be exposed as a pervert in front of the university, so I will continue the act. I hope they don’t ask me to go swimming or something."
    scene bg calleinglesadia with fade
    "With that we set course towards the dorms. Rose leading me by the hand. Damn, girls don’t really mind physical contact between them. I try not to look too embarrassed, without success."
    show rose chall with dissolve
    "She looks at me for a few seconds, her stare is piercing my soul."
    $ rose = "happyclosemo"
    show rose with dissolve
    "She keeps walking without saying a single word, we are halfway towards our destination."
    $ rose = "sad"
    $ sadrose='sad'
    "After walking for awhile, she finally breaks the silence."
    r "I actually thought you were antisocial."
    r " I mean, today in the morning you actually ran away from the girls at the dorm.{w}"
    $ sadrose='not'
    $ rose = "happy"
    extend" But now that I see how flustered you are I can’t do anything but chuckle a little at the thought."
    j "Actually,{w=.5} I was kinda scared this morning."
    
    $ rose = "happy2"
    r "Scared?{w=.3}"
    $ rose = "surp"
    extend" Why?"
    
    menu: 
        "There was a cockroach on my bathroom this morning.": 
            $ g = g + 1
        "Women scare me.":
            $ s = s + 1
        "I didn’t sleep well because there was someone watching me last night.":
            $ n = n + 1
    $ rose = "surp"
    "Rose is kinda surprised by my answer, but remains silent and just walks in front of me, she didn’t even flinch."
    show rose with dissolve
    scene bg edifapt with fade
    "After a few minutes we arrive at the dorm, we part ways at the stairs because her room is to the right wing and mine to the left."
    hide rose with dissolve
    "I’m emaciated. I check the clock. 3:45 pm."
    j "Damn, it’s not even dark yet…"
    j "Well I didn’t sleep much last night,{w} so the time is as right as it’s going to get."
    scene black with dissolve
    "It doesn’t take me long to fall asleep."
    
    "*Day 2*"
    "Alarm" "*Riiing!!*" with Shake((0, 0, 0, 0), 0.5, dist=15)
    scene bg cuartodorm with fade
    j "Damn, it’s morning already? Didn’t even had time to eat last night."
    scene bg pasillodorm with fade
    "I get ready as fast as I can and sneak up to the door to see if any of the girls is awake."
    "Deserted."
    "I take the opportunity and dash out of my room. As I am going downstairs my stomach reminds that I am actually starving."
    scene bg cafeteria with fade 
    "I turn left on the building’s lobby and access the cafeteria."
    "It doesn’t take long for me to order some pancakes."
    "I feel something on my back so I try to turn to see what is it but before I can even check, something blinds me."
    
    scene bg black with dissolve
    u "Guess who?"

    "I’m shocked for a sec there but then I remember that I don’t know anyone besides Rose,{w=.3} so the answer is obvious."
    
    j "Rose, clearly the only early game prankster I know."
   
    scene bg cafeteria with fade
    $ rose = "happy2"
    show rose with dissolve
    r "You got me there!"
    $ rose = "happyclosemo"
    show rose at pop
    extend" hahahahaha!"
    $ rose = "challenging"
    r "Not fair, probably you didn’t even know anyone else on the dorm!"

    "I cringe a little, she notices so I get a little bit more flustered."
    $ rose = "sad"
    $ sadrose='sad'
    r "Exchange students sure are weird, why are you red all the time?"

    menu:
        "I’ve never been approached by such a beautiful woman before":
            $ g = g + 1
            $ s = s + 1
            $ ans = 1
            j "I’ve never been approached by such a beautiful woman before."
        "I’m actually a guy":
            $ b = b + 1
            j "I’m actually a guy"
            $ ans = 2
        "I’m actually kinda drunk at the moment":
            $ n = n + 1
            j "I’m actually kinda drunk at the moment."
            $ ans = 3
    show rose with dissolve
    "Her eyes are wide open. She cannot believe what I just said. But  she calms down after a few seconds."
    $ sadrose='not'
    if ans == 1:
        
        $ rose = "surp"
        $ roseblush = "blushing"
        show rose at pop
        r "Well, as long as you don’t hit on me!"
        $ roseblush = "notblushing"
    elif ans == 2:
        ''
        $ rose = "madO"
        r "You silly goof, how am I going to believe that?!"
    elif ans == 3:
        $ rose = "surp"
        r "Not possible, you’ve only lived on the dorm for a day."
    $ rose = "happy"
    "Chatter after that goes without events so we head to our classroom."
    $ rose = "happy"
    j "Damn, Calculus in the morning really sucks."
    $ rose = "naughty"
    r "Well we can skip classes if you want..."

    "She says it with the most mischievous smile I’ve ever seen in my life."

    j "That is not a proper answer lady, what if we get caught?"
    $ rose = "sad2"
    $ sadrose='sad'
    "She kinda looks sad at my answer, like a little puppy after being scolded."
    "I feel a little bad that I turned her down without even thinking in my response. "

    j "Damn, don’t do those puppy eyes, let’s go get some ice-cream at the mall{w=.3}.{w=.3}.{w=.3}."
    $ sadrose='not'
    $ rose = "happy2"
    show rose at pop
      
      
    "Suddenly she looks rejuvenated by my answer."
    "In fact she is so happy that I start to question if she really was sad at first or if it’s was just an act."
    "Well can’t do anything now, so I accept my destiny."
    hide rose with dissolve
    hide cafeteria with fade
    scene bg calleinglesadia with fade
    "We start to walk on the same direction to the University, but turned right a few blocks before."
    scene bg mall with fade
    "After looking at the mall I think that just a really disoriented person would miss it, it has a huge Mall sign at the top and it’s surrounded by flat 1 level houses."
    
    "We walk in and proceed to search for the ice-cream shop. It doesn’t take us long because it’s by the entrance of the second floor."
    
    "Rose is always walking in front."
    "I wonder why she doesn’t like me to be ahead of her, maybe she feels like it’s her duty as an old-established student."
    "I don’t mind though, the less time she spends observing me, the less I’m likely to get caught."
    scene bg heladeria with fade 
    r "Can you give me a Vanilla cone please sir?"

    "The old man produced said cone with such dexterity that I’m actually perplexed."
    "I’m so surprised I forget it’s my time to pick a cone, so Rose shakes me out of it standing closely in front of me."

    j "What.. Oh yes the flavour, I’ll have Vanilla-Strawberry flavour please"

    olm "As you wish sweetie"

    "Damn it doesn't feel good when even the old man mistakes you for a woman."
    "For a second there, looking on the bright side, if he said otherwise he would’ve blown my cover."

    "I turn around with my cone and proceed to take a sit on the bench that Rose is sitting in."
    "I don’t know why but she is staring at my cone intensely."
    $ rose = "challenging"
    show rose with dissolve
    j "Do you want to try it?"
    $ rose = "happy"
    r "It’s not that, I’m kinda confused that you picked those two flavours."
    r "I mean, probably one will be stronger than the other and it will end up tasting just like it…"
    
    j "Well that’s not how I see it, let me explain."
    $ rose = "surp"
    j "It’s not two different things, they are part of one whole, like yin and yang they are not trying to dominate the universe but coexist in balance."
    j "Sure Vanilla is great alone and so is Strawberry, but together is where they really shine."
    
    "I don't know if what I said was that weird but Rose is staggered. It takes her a few seconds to recompose herself."
    $ rose = "happy"
    r "Yeah I understand what you mean. I’m not feeling well right now so maybe I should go back to my room…"

    j "Do you want me to escort you?"
    $ rose = "challenging"
    r "No. I’m fine, you should probably head back to our second class, maybe you can catch it up"

    "I’m kinda confused but it doesn’t matter as Rose just stands up and starts walking towards the exit."
    hide rose with dissolve
    "I can only watch her as she finally exits the building. Damn she is pretty. But that feeling doesn’t last long because I realize that I may have fucked up something with my analogy."
    "I spent the next half an hour trying my best to understand her without success."

    j "Damn girls sure are mysterious"

    "Well I’ve got to make up with her somehow."

    "After a few minutes of critical thinking I decide to buy her something. I don’t know what she likes but whatever, can’t get any worse, right?"
    scene bg mall with fade #alv
    "I spend the rest of the day searching for something, finally I decide to buy her some chocolates."

    j "I’ve never met a sane person who doesn’t like chocolate, this should be alright"
    scene bg calleinglesadia with fade
    "I proceed to buy the chocolate at the convenience store and start to head back to my dorm."
    scene bg edifapt with fade
    "Time sure flies fast, after a few minutes I’m standing in front of the dorm, didn’t even notice the time it took me to get there."
    "Whatever, I better give her the chocolate today, sure, it’s dark but, she’s probably still awake."
    scene bg pasillodorm with fade
    "I walk into the dorm and to my surprise there’s no one on the lobby. Probably all of them are already asleep. I take the stairs and in a flash I’m in front of her room."
    "I hesitate for a second then I proceed to knock on the door. "

    "No answer."

    "Maybe she is not at home, so I turn around. As I was taking my first step forward I felt something around my neck."
    "I raise my hand to it and touch it for a second. It seems to be a scarf."

    "When I try to turn around the scarf tightens up, I can’t breathe well anymore."

    u "What do you want with me woman?"

    "Wait a second, I know that voice, it's Rose’s, isn’t it?. I turn around to confirm it"
    $ nrose = "mad5"
   
    show nrose with dissolve
    "I was right, it is her."

    j "Rose why are you doing this…?"

    "Wait a second why is her hair red? Am I already asphyxiating?"
    "No{w=.3}.{w=.3}.{w=.3}.something's not right."
    $ nrose = "mad"
    j "I just wanted to give you this chocola--{w=.8}{nw}"

    "I haven't even finished my question when she snaps the bar of chocolate out of my hand.{w=.5} Then as quick as lightning, she closes the door of her room."
    "Then I hear something muzzled on the distance."
    $ nrose = "mad2"
    r "Keep the scarf, I was going to give it to you anyway,{w=.5}"
    $ nrose = "mad3"
    extend" you seemed cold this morning..."
    hide nrose with dissolve
    "The rest is inaudible, but I think I got the important part anyway. I check the scarf, it's hand made with red and white candy floss, very warm at the touch."
    "I don’t know what to think I’m more confused now that I was at the mall."
    scene bg cuartodorm with fade
    "Anyway, I’ll ask her tomorrow about it. For now I’ll just go to sleep."

    "It doesn't take me long to get ready to sleep. As I jump in bed, wrapped in the warm Red-White scarf that Rose gave me, I quickly fall asleep."
    hide bg cuartodorm with fade
    scene bg black with dissolve
    "*Day 3*"
    scene bg cuartodorm with fade
    "Alarm" "*Riiing!!*" with Shake((0, 0, 0, 0), 0.5, dist=15)
    "Thank God for that noisy alarm I selected. Just when my nightmare was getting out of hand, it woke me up."

    "I quickly get up and in less than 20,{w=.5} I’m ready to go out of my room.{w=.5} As I open the door a chilly breeze hits me in the face, so I close the door quickly."

    "I remember that scarf Rose gave me yesterday so I grab it and wrap it around my neck."
    scene bg pasillodorm with fade
    "I gaze at the clock for a second. I’m running late for my first class. I quickly open the door and start walking rather fast towards the stairwell."
    "*Bump!!*" with Shake((0, 0, 0, 0), 0.5, dist=15)
    "I’m so troubled by yesterday’s turn of events that I didn’t notice someone standing after a corner and end up bumping into her." 

    $ rose = "sad"
    $ sadrose='sad'
    show rose with dissolve
    j "Sorry I didn't notice you were standing there, my bad."

    "As I get up, I notice who is it that I bumped into."

    "It’s Rose."

    "I’m embarrassed so I quickly look away from her. But she's staring at me. I start to get more nervous, is there something in my face?"
    
    "After a couple of uncomfortable seconds she breaks the silence."

    $ rose = "surp"
    r "Where did you get that scarf?"

    "I’m confused by the question so I don’t reply immediately."

    j "What do you mean?{w=.3} You gave it to me yesterday when you were on that foul mood…"
    $ sadrose='not'
    $ rose = "surp2"

    "I look up so I can see her face for a second. Her eyes are wide open like plates and she is frozen, paralyzed."
    
    hide rose with Dissolve(0.25)
    "She wakes up from the shock and tries to escape,"
    $ sadrose='sad'
    $ rose = "sad3"
    show rose with Dissolve(0.25)

    extend" but I’m faster so I grab her by the wrist before she can even start running away."
    
    "I turn her around so I can see her face again, she is crying. I don’t know what to do so I try to comfort her the only way I know."
    "I pat her on the head a couple of times and wipe her tears with my sleeve."
    $ rose = "sad2"
    j "Hey, everything is going to be alright, just tell me what happened when you are ready, ok?"
    $ rose = "sad3"
    "At this moment she loses control over her emotions and starts to cry intensely."
    
    r "I’m sorry…. I will."
    hide rose with dissolve
    "At this point we are so late for our first class that there is no point in hurrying anymore. We walk calmly towards the University. I don’t let go her hand, she needs this."

    "After a prolonged silence in our journey she mumbles something."
    $ rose = "sad"
    show rose with dissolve
    r "I’m sick and I’m not in control of what I do sometimes. Didn’t even remember what I did yesterday. I hope you can forgive me…"

    j "Don’t trouble yourself with it Rose, anyway, you gave me this beautiful scarf."
    $ rose = "happy"
    "Finally, she regains her usual silliness and laughs a little. It’s better when she is not sad."
    hide rose
    show bg universidad with fade
    "Classes at the University elapse without any memorable events. Boring day. I’m saved by the bell because I was falling asleep."
    show salonclase with fade
    "I get up and gather my things, doesn’t take me long because I don’t use notebooks, just a reader and a tablet. As I approach the exit someone tugs my sleeve lightly."
    "It’s Rose."
    $ rose = "sad"
    show rose with dissolve
    r "I want to compensate you for understanding my situation, maybe we can go somewhere where we can talk more comfortably."

    j "Oh, I got just the right place in mind!"
    hide rose
    hide salonclase with fade
    scene bg mall with fade
    "I take her by the hand to the Mall, her hands are as cold as ice so I lend her my hand gloves. Even when one is being mistaken as a girl one must not let a young woman suffer."
    scene bg cafe with fade
    "We enter a cafe and take a sit in a table close to the window, we can see everything from here. Good thing that it’s almost deserted, just an elderly couple sips some tea on a corner."

    "We small-talk for 20 minutes or so, when Rose decides to acknowledge our serious matter."
    $ rose = "sad"
    show rose with dissolve
    r "Today I told you that I was sick, well{w=.3}.{w=.3}.{w=.3}.{w=.3}that is not entirely true."
    $ rose = "sad"
    r "You see,{w=.3} remember we are not normal humans, June. We were created on labs by scientists."

    "I nod so she knows I understand what she means."
    $ rose = "surp"
    r "You see I was one of the first successful tests and have some ‘bugs’ on my DNA.{w} If you can call them like that."
    $ rose = "sad2"
    r "I’m one person at night and another one by day…"
    
    r "The other Rose…she is not a kind person."
    $ rose = "madclose"
    r "She’s dangerous."
    hide rose with dissolve
    "She goes on with more deep information about herself, but that first part was so intense that left me thinking for a while."

    "After a while we’re just sipping our near-cold drinks and staring out the window. I decide to tell her what I think about her problem."
    $rose = "sad"
    show rose with dissolve
    menu:
        "You cannot deny a part of who you are":
            j "Why fight with a part of yourself, there cannot be a Rose without the day Rose and night Rose. You may have suffered with love once but you don’t give up on a whole emotion because of one bad experience" 
            j "I like you the way you are, with flaws and everything"
            $ b = b + 1
        "Don’t give up hope, you can be cured and live a normal life":
            j "Don't’ give up just yet."
            j"Medicine advances so quickly that maybe in a couple of years you can be treated and finally live a normal life."
            j"Hope is the last thing that dies and I’ll be right here for you, Rose."
            $ g = g + 1
        "I don’t feel comfortable talking about this kind of stuff with girls, sorry":
            $ s = s + 1
    
    if s >= 3:
        jump bad
    elif b >= 2:
        jump bad
    elif g >= 2:
        jump good
    elif n >= 2:
        jump neutral
    else:
        jump bad
    
    
    
    return
    
    
#Bad Ending
label bad:
    $ rose = "madfrown"
    "Rose seems confused at my answer, but tries to hide her confusion behind her drink. She takes a few slow sips and looks out the window."
    "We stay still for a few seconds, then she breaks the silence with a quick gaze and a puzzling statement."
    r "If I didn’t know you are a girl, I would definitely see you as a guy{w=.3}.{w=.3}.{w=.3}."
    "I don’t know how to take this, maybe she discovered my secret way too fast.{w} I should take this opportunity to clear the mistake they made at the dorms{w=.3}.{w=.3}.{w=.3}."
    j "You got me… They made a mistake at the dorms, I’m actually not a girl, but I think the photo I sent on my registry application fooled them." 
    j "Maybe I should cut my hair, sadly I like it the way it is right now."
    $ rose = "challenging"
    "No emotion. She just keeps looking at me while I finish my explanation. I don’t know what to do, she looks frozen in time."
    "About 20 seconds go by...she picks up her cup and finishes her drink."
    hide rose with fade
    "She stands up, thanks me for the coffee and exits the shop."
    "I don’t know how to react so I sit there, just wondering if I made a mistake or not. Time passes by slowly. After I finish my coffee I head back to my room."
    "I'm confused, did I say something wrong?"
    scene bg calleinglesadia with fade
    "The way back is as tedious as a math exam, takes me longer because I doze out on the crosswalks that are on the way."
    "Maybe I should leave."
    "I don't know if Rose plans to tell that old lady from the building that I'm actually a guy."
    "I'm scared, my fate is at the hands of someone I barely know and that is pretty bad."
    scene bg edifapt with fade
    "Finally I arrive to the dorm, I'm surprised, it is this empty. Then I remember that it is a student dorm and that everyone is probably still at campus."
    j "Well I hope Rose is still in her room. I should apologize to her as soon as possible."
    scene bg pasillodorm with fade
    "I climb up the stairs as slow as I can, but it's just delaying the inevitable."
    "Finally I arrive to her room. I'm frozen there. Thoughts start rushing in my head. What if.. well worst case scenario I get expelled."
    "I knock at her door effusively but nobody answers. After a few minutes, I give up."
    j "Maybe she's still at campus and actually attended our next class, unlike me."
    "Well, I'm pretty tired. Stressful days make me tired for some reason."
    scene bg cuartodorm with fade
    "I get into my room and just slam the door, I'm pissed by the turn of events. I don’t even want to put on my pajamas, I'm too tired for etiquette."
    scene black with fade
    "Sleep catches up to me in no time. The stress is so immense that soon I'm fast asleep."
    "*bump*"
    "There is a noise coming from the door. It is so loud that it wakes me up."
    "What time is it right now?"
    "I take a look at the clock on the wall. 3:42 am. What on earth is so loud that it woke me up?"
    "Then I feel it. The cold. A chilly wind comes from the entrance."
    "Then I notice it. The door is open and someone is approaching."
    "It takes me a couple seconds to determine who it is, but as soon as the moonlight is reflected on her head the answer is clear."
    "It is Rose."
    j "How did you get in here?, the door was locked!"
    $ nrose = "mad4"
    show nrose with dissolve
    r "A few locks won't stop what is coming to you."
    $ nrose = "mad"
    r "You thought you could deceive me?, Did you forget that I'm like this at night?"
    $ nrose = "mad6"
    r "Well, you won't be fooling anyone else from now on…"
    hide nrose
    "After she stops talking she rushes to me. She is too fast for me to react. I'm still half asleep so she quickly overcomes me."
    r "It seems fitting for you to die by the gift I made for you."
    "Quickly she reaches out for the scarf she knitted for me and wraps it around my neck."
    "I feel the air escaping my body. I try to inhale but I can't."
    "I've brought this upon myself. Seems fitting I end up this way."
    "Suddenly everything goes black."
    "Finally I'm at ease, maybe in the next life I won’t be this careless…"
    scene bg black with fade
    call credits
    return
    
#Good Ending
label good:
    $ rose = "happy"
    $ sadrose='not'
    "Rose smiles a little after my answer, but happiness doesn’t last long enough as she soon starts to weep a little."
    $ rose = "closetears"
    j "What did I say?, Did I hurt you in someway?"
    $ rose = "happytears2"
    r "No, it’s just, you gave me hope for a minute there…"
    r "You see{w=.3}.{w=.3}.{w=.3}. Doctors said that my condition was untreatable{w=.3}.{w=.3}.{w=.3}."

    j "That may be the case today but together we can search for it someway"
    j "We are on a biology-oriented university for that matter"
    $ rose = "sad4"
    $ sadrose='sad'
    "It seems I succeed in calming her down a bit. Maybe we should go somewhere else, I feel like she opened to me in some way maybe I should make up for that."

    j "Hey , I know we’ve known each other for like a week, but you know you can trust me… anything you need that I can help you with you can tell me."
    $ rose = "sad2"

    r "I know…"

    "I should really change the mood someway or the rest of the evening is going to be pretty unpleasant."

    j "Maybe we can hit up the theater and watch a movie or something{w=.3}.{w=.3}.{w=.3}."
    $ rose = "surp"
    "She seems confused for a second there, but then I remember something that maybe I haven’t told her yet. Yes you guessed right, she still doesn’t know I’m a guy."

    j "I have a confession too Rose…"
    $ rose = "surp2"

    r "Huh?"

    j "You see, the day I came to England they made a mistake on my University inscription, the truth is that I’m a man…"
    $ rose = "surp"
    "Her eyes widen a bit but then she recovers her composure. A few seconds go by but still no answer from her. I start to worry."
    hide rose with fade
    "I stand up and face the door, maybe it is better for me to get out. "

    "I cannot move, there is something holding me up, I quickly notice that Rose is holding up my sleeve and she wont let me advance."
    $ rose = "madfrown"
    $ sadrose='not'
    show rose with dissolve
    "She points at the place where I was sitting, so I assume she want’s me to sit down over there. After I do it, she takes another few seconds and starts talking."

    r "You see… I knew from the first day that you were a guy."

    j "Wha.. how?"
    $ rose = "happy"
    r "Well{w=.3}.{w=.3}.{w=.3}. nobody noticed it but you entered the dorm wearing your casual clothes, and they were man-looking, so I suspected it."
    r "Later that night I went to check,{w=.5} well actually the other Rose went to check,{w=.5} and we found your ID on your luggage..."
    r "So basically we knew."

    j "You checked my backpack?!?"
    $ rose = "sad2"
    r "Sorry I just couldn’t resist."

    j "Nah I was the one who was wrong, I should’ve told you from the start."
    j "So, we are even,{w=.5} I suppose."
    $ rose = "happy2"
    r "Yup… Nice to meet you."
    
    j "Stop fooling around you doofus, how about that movie then?"
    $ rose = "laughing"

    r "Damn, straight for the vein, guys have less tact than I’ve thought{w=.3}.{w=.3}.{w=.3}."

    "I think I made a funny face at that statement because she looks another way quickly."
    $ rose = "happy2"
    r "Okay I’ll go out with you, just stop looking like a stray dog in front of a bakery please!"
    $ rose = "sad"
    r "Before we go, let me go back to the dorm, I’m kinda tired at the moment and want to take a nap"

    j "Okay then, let's head back to our rooms"
    hide rose with fade
    scene bg calleinglesadia with fade
    "The journey back to the dorm is as monotonous as always, but has a different tone now. She knows my secret and I know hers. There is an invisible bond between us that tie us somehow."
    scene bg edifapt with fade
    scene bg pasillodorm with fade
    scene bg cuartodorm with fade
    "We enter the building, climb up the stairs and part ways on the hall. I enter my room and go straight to sleep. This time I set up an alarm because I don’t want to screw up this date."
    scene bg black with fade
    a "***beep! beep!***" with Shake((0, 0, 0, 0), 0.5, dist=15)
    scene bg cuartodorm with fade
    "That annoying alarm wakes me up. After I come back to my senses it is not so bad, I have to get ready fast or I’ll be late."

    "I get ready in no-time, and on top of it I pick up my thick jacket, it seems like this evening is going to be chilly."
    scene bg pasillodorm with fade
    "I walk over to Rose’s room and knock the door twice, it only takes me enough time to blink because she opens it faster than lightning."
    $ rose = "happyclose"
    show rose with dissolve
    "I’m caught out of guard, so I say the first thing that comes to my mind."

    j "Hey, you ready?"
    $ rose = "happy2"
    r "As ready as I’ll ever be."
    hide rose with fade
    scene bg edifapt with fade
    scene bg calleinglesadia with fade
    "We walk out of the dorm and as we are walking down the street Rose steps in some frozen water, she almost falls off, but I manage to catch her on time."

    "I take the opportunity, I don’t think I’ll another one this good tonight."
    $ rose = "surp"
    show rose with dissolve
    j "Careful girl, I don’t want to head up to the hospital tonight, I have an idea, why don’t you let me hold your hand so if you fall, we fall together?"
    hide rose
    "Rose looks quickly another way, I don’t know what expression she makes but I go for it anyway, I mean what can I lose?"

    "She doesn’t let me hold her hand as she quickly withdraws them when I touch her."

    "I'm hurt inside, frozen in place. God please take me right now."

    "She approaches me, and grabs my arm up to my shoulder, she is so close I can even smell her hair. Floral essence, probably roses. Would make sense."
    $ rose = "tsundere"
    show rose with dissolve
    "I take a look at her, she is so flustered she may pass out any second, but I cannot point that out, my manliness won’t let me do so."

    "We walk slowly, mainly because we want to stretch up the time we have together the most we can, using the excuse that we may trip over some ice."
    scene bg afueracine with fade
    hide rose
    scene bg lobbycine with fade
    "We arrive at the cinema, it’s dawn when we pick up our tickets for the movie, it wasn’t much of a choice, the only two movies this small town had were a horror one and a futuristic dystopian type of movie."

    "It takes us some time to order our popcorn because the cashier was slow as a snail. After that, we go to our theatre-room. It’s almost empty, I’m not really surprised considering that nobody was buying tickets."
    scene bg adentrocine with fade
    "We sit around the rows that are on the middle because we don't want to be too close to the screen."

    "At the start of the movie everything is ok, Rose seems to be doing ok, but then a scary scene pops up and she freaks out: I try to calm her a little but nothing seems to work. It’s then when I decide to grab her hand just to calm her down."
    scene bg lobbycine with fade
    "It seems to work so I keep it for the rest of the movie as well. After the movie finishes we leave as usual and go to the lobby, it is late at night, the movie took more than we expected so it is deserted."
    scene bg afueracine with fade
    "We go outside and it is pitch dark, can't even see my hands when I hold them right in front of me. Then I remember that Rose changes whenever it is night or day so I turn around as fast as I can and start searching for her."
    $ rose = "surp"
    show rose with dissolve
    "It doesn’t take me long, she is standing at the theatre’s entrance, just there, shocked, staring at the sky."

    "I approach her but she doesn’t seem to notice me so I gently take her hand."

    j "What happened, did you happen to see a ghost or something?"
    $ rose = "sad4"
    "She snaps out of it, then just looks at me and her expression changes completely. She is now borderline crying."

    j "What, did I say something that made you upset?"

    "She mumbles something but I can barely understand anything. I come closer to her and hug her so she knows I'm here for her if she needs me. "

    "She whispers in my ear: "
    $ rose = "closetears"
    $ sadrose='sad'
    r "I’m shocked, it is now nighttime, but I’m still my normal self"

    j "How is that even possible!?"
    $ rose = "happytears"
    $ sadrose='not'
    r "I don’t really know, but today was a special day for me, I shared memories with someone I care about… I think you made this possible"
    r "The truth is that I care about you… No. That’s not true, since the moment that I first saw you, you moved something inside me."
    r "I started to look forward to our next meeting, I could barely sleep. But today all my doubts were washed away…"
    $ rose = "surp2"
    $ roseblush = 'blushing'
    r "I realized today that I’m in love with you."

    "I don’t even hesitate, I want her to know that I feel the same way she does, but the words don’t come out."
    hide rose with fade
    "So I do what I feel would let her know how I feel about her."

    #Kiss Scene
    $ rose = "happytears2"
    show rose with dissolve
    j "I want to know you better, I don’t care if you are missing parts, for me you are complete and that is what makes you perfect."
    hide rose with fade
    scene bg black with fade
    call credits
    return
    
label neutral:
    $ rose = "surp"
    show rose with dissolve
    "Rose seems to be confused at my answer, she doesn’t even acknowledge anything. The rest of the evening we talk about things that have little to no impact whatsoever, after our chat is over I pay for our drinks and head out for the exit."
    hide rose with fade
    scene bg calleinglesadia with fade
    scene bg edifapt with fade
    scene bg pasillodorm with fade
    "We walk back to the dorms, nothing special happens all the way anyway. We climb up the stairs towards our rooms and split up when we are at our floor."
    scene bg cuartodorm with fade
    "I enter the room feeling kinda sad, maybe I did something that Rose didn’t like or maybe something that made her upset. I really don’t know at all."
    scene bg black with fade
    "Night comes but I'm not sleepy at all, maybe I’ll go for a walk somewhere outside. So I get ready, pick up my thick jacket and my scarf and head right outside."
    scene bg pasillodorm with fade
    "Everyone is asleep, not surprising knowing it’s around  like 3 am or something. On the back of the dorms there is a little park with umbrellas so I take a sit around there."
    scene bg exteriorbnch with fade
    "I pick up my phone and start to play a card game in it, ah it feels much better when you are outside, I’m not really claustrophobic but just the fact that I’m outside that little room makes me feel better."
    "Suddenly I feel like there is someone behind me."
    "I quickly get on guard and turn myself around but after my eyes get accustomed to the darkness I can say who is it."
    "It’s Rose."
    $ nrose = "mad1"
    show nrose with dissolve
    j "Darn, you scared me Rose, please don’t do that again!"
    $ nrose = "naughty"
    r "But you look cuter when you are scared like that."
    j "Wha..?"
    "I figure it out, it’s the other Rose, day Rose doesn’t normally behave like this."
    $ nrose = "happy"
    r "Don’t you like nights?, I find them very vexing, this is the only time I have to be my real self."
    j "So you consider yourself as the real Rose then."
    $ nrose = "mad4"
    r "Then explain why I have different feelings than the other Rose."
    $ nrose = "mad"
    r "Some things don’t bother her but they piss me off."
    r " Sometimes she does something she regrets but I think they are Ok. I’m always present in her even If I cannot make anything to change the course of action."
    $ nrose = "mad2"
    r "I’m my own self, trapped inside her, powerless."
    j "Well if it makes you feel better I like you as well, you may be evil and sadistic but those are your own traits and if you consider yourself as another person so will I"
    $ nrose = "happy2"
    r "Considerate for someone who the other one despises"
    j "So the other Rose hates me… well I wasn’t for her when she needed me. I got what I deserved. I don’t know but it saddens me deeply somehow."
    $ nrose = "bored"
    r "Huh, you talk like I care how you relationship with her is going. Go cry to your room alone, I won’t comfort you in any way if that’s what you expect."
    $ nrose = "normal"
    r "I’ll take my leave, remember to close the gate so they don’t know you were outside this late."
    j "Wait, where are you going this late at night, It’s not safe for you to be on the streets."
    hide nrose
    "She firmly ignores my advice and keeps on walking towards the street. I cannot let her go alone, I have to protect her somehow."
    "So I decide to follow her at distance, so she doesn’t know that I am protecting her."
    scene bg calleinglesanoche with fade
    "Everything is calm so I can relax a bit, no one’s on the street so probably she will return safely after she is done with whatever it is she is planning to do."
    scene bg puente with fade
    "She walks towards an old bridge, but she decides not to go over it, instead she takes some small rusty stairs on the side. The stairs go under the bridge, honestly, what is she thinking?"
    "I catch up to the bridge’s side and take a look inside, what I see amazes me. She is giving food she had on her backpack to a homeless family."
    "How is it even possible, this Rose could easily pass up for like a serial killer or something. This made me realize that appearances may deceive me but if I look closer maybe I’ll find the truth hidden somewhere."
    "Rose is quickly done with the family and starts walking towards where I’m hiding, so I climb the stairs as fast as I can, luckily I’m fast enough so she doesn’t notice me hiding on a bush."
    scene bg carrosospechoso with fade
    "She starts walking back to the dorm but I notice something’s off. There is a car parked down the road. The car looks suspicious so I start approaching Rose to be as close as I can be."
    "Suddenly a man pops out of the car and grabs her by the arm, I don’t have much time to act so I run towards them. I catch up to them, he is still struggling on trying to get her on the passenger's seat."
    "I punch the guy in the face so hard he hits the back of his head with the door. He is knocked out."
    j "Rose we gotta get out of here fast!"
    scene calleinglesanoche
    $ nrose = "mad2"
    show nrose with dissolve
    "She is still baffled at the incident so she appears like she’s on shock. Kinda weird if you ask me because this Rose’s blood is as cold as ice."
    "I grab her forearm firmly and we start running to the dorms. We get there in no time."
    hide nrose
    scene bg exteriorbnch with fade
    "We take some time to recover some breath but we are exhausted because of the run. We stay like that a couple of minutes in silence, Rose is the one that breaks the silence."
    $ nrose = "mad5"
    show nrose with dissolve
    r "Why were you following me?"
    $ nrose = "sad"
    j "I just couldn't let a young woman go out this late at night, no matter if you are cold to me you are still precious to me."
    $ nrose = "sad2"
    "As I finish my statement Rose explodes, She is crying seas. I don’t know what to do so I hug her firmly. She gets a hold of herself and pushes me away. She wipes her tears slowly."
    $ nrose = "sad3"
    r "Remember when I told you that the other Rose made things that she liked but I disliked?"
    j "Yes, I remember, you told me just a few hours ago.."
    $ nrose = "mad5"
    r "That's not the point I'm trying to make you smartass."
    "She gives me such a mean look that I may be facing satan himself, but it quickly changes to a more comprehensive one."
    $ nrose = "mad5"
    $ roseblush = "blushing"

    r "What I’m trying to say is that the other one wanted you to stay away from her, and I don’t want that… Do you understand?"
    j "What are you trying to say, that you don't dislike me as the other Rose?"
    $ nrose = "mad0"

    r "You fool, are going to make me say it don’t you!?"
    $ nrose = "mad"
    r "I think I’m in love with you, alright? I don’t want you to leave my side, do you understand?"
    "She approaches me, we are facing each other, just a few centimeters away from each other."
    "Suddenly she takes the initiative and kisses me, just a short one to see if I’m into her, I so I decide to assure her that I like her."
    "I kiss her again, longer this time."
    $ nrose = "sad"
    $ roseblush = "notblushing"
    "After it she kinda looks sad so I have to ask her why."
    j "Isn’t this what you wanted?"
    r "You probably don’t even like me. I mean, I’m different from the Rose you know, I have more flaws, and nobody likes the way I am"
    j "Those things you call flaws are the things that make you who you are, and I like it all"
    $ nrose = "sad2"
    r "But I can't see you everyday, how can I be with you?... why did I have to be the night one and not the day one?"
    j "Love knows no boundaries Rose, I’ll be here with you every night for you are the Rose that matters to me."
    scene bg black with fade
    
    call credits
    return

label credits:
    $ credits_speed = 25 
    scene bg final 
    with dissolve
    show theend:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(1)
    hide theend
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(1)
    hide thanks
    show extra:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide extra
    return

init python:
    credits = ('Character Artist', 'Russel Alfonso'), ('Backgrounds', 'Yasmin Chavez'), ('Backgrounds', 'Ivette Cardona'), ('GUI', 'Andrea Cordon'), ('Script', 'Jose Rodolfo Perez'), ('Coding', 'Sebastian Recinos'), ('Spell Check', 'Samantha Duarte'), ('Spell Check', 'Cristian Perez')
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}" + renpy.version()
    
init:
    image cred = Text(credits_s, text_align=0.5)
    image theend = Text("{size=80}The End", text_align=0.5)
    image thanks = Text("{size=80}Thanks for Playing!", text_align=0.5)
    image extra = Text("{size=60}Don't Forget to get all the endings!", text_align=0.5)





    


from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from colour import Color
from manim_voiceover.services.azure import AzureService
from manim_voiceover.services.coqui import CoquiService
import os

class votest(VoiceoverScene):
    def construct(self):
        os.environ['KMP_DUPLICATE_LIB_OK']='True'
        
        self.set_speech_service(
            GTTSService(lang="en", tld="com", transcription_model='base')
        )
        # self.set_speech_service(
        #     AzureService(
        #         voice="en-US-AriaNeural",
        #         style="newscast-casual",
        #     )
        # )
        circ = Circle()
        square = Square()


        with self.voiceover(
            text="""Hello. <bookmark mark='A'/> Right now I am drawing a circle. 
            <bookmark mark='B'/> And now it is going to transform into a square. 
            <bookmark mark='C'/>And that is it."""
        ) as tracker:
            self.wait_until_bookmark("A")
            
            self.play(Create(circ), run_time=tracker.time_until_bookmark("B", limit=1))
            self.wait_until_bookmark("B")
            
            self.play(Transform(circ, square), run_time=tracker.time_until_bookmark("C", limit=1))
            self.wait_until_bookmark("C")
            self.play(FadeOut(circ))
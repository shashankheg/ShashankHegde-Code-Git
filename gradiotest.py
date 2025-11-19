from logging import PlaceHolder
import gradio as gr
from yaml import BlockSequenceStartToken

def greet(Name):
    return "Hello, " + Name + "!"


def BMI_Calaulator(Name, height, Weight, Feeling):
    BMi_value = Weight/((height/100**2))
    result_emiton = "Great" if BMi_value<30 else "Needs improvement in your lifestyle"
    output_str = "Hello" + Name + "..\n your BMI is ...." +str(BMi_value)
    txt ="Happy " if Feeling else "Sad"
    return (output_str,result_emiton,txt)

demo = gr.Interface(fn=BMI_Calaulator,
                    inputs =["text","slider",gr.Slider(0,200,label="Height"),"checkbox"],
                    outputs=["text","text","text"],
                    theme=gr.themes.Glass(),
                    )
demo.launch(share=True)
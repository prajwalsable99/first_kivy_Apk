import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

#for function of app
import cmath

class my_layout(GridLayout):
    def __init__(self,**kwargs):
        super(my_layout,self).__init__(**kwargs)
        self.cols=1
        self.inr=GridLayout()
        self.add_widget(Label(text="ax^2 + bx +c=0"))

        self.inr.cols=2
        self.inr.add_widget(Label(text="quadratic eqn Solver:"))
        self.inr.add_widget(Label(text="by Prajwal Sable"))

        self.inr.add_widget(Label(text=" a:"))
        self.a=TextInput()
        self.inr.add_widget(self.a)

        self.inr.add_widget(Label(text=" b:"))
        
        self.b=TextInput()
        self.inr.add_widget(self.b)
        
        self.inr.add_widget(Label(text=" c:"))
        self.c=TextInput()
        self.inr.add_widget(self.c)
        
        

        self.add_widget(self.inr)


        self.calculate=Button(text="calculate")
        self.calculate.bind(on_press=self.calc)
        self.add_widget(self.calculate)
        
        self.results="prajsa99@gmail.com"
        self.res=Label(text=self.results)
        self.add_widget(self.res)
        
   

        

    def calc(self,event):
       
        self.remove_widget(self.res)
       
        

        
  


        
        try:
            a=float(self.a.text)
            b=float(self.b.text)
            c=float(self.c.text)

            d=(b**2)-(4*a*c)
            r1=(-b-cmath.sqrt(d))/(2*a)
            r2=(-b+cmath.sqrt(d))/(2*a)
            
            a=round((r1.real),2)
            b=round(r1.imag,2)

            c=round((r2.real),2)
            d=round(r2.imag,2)

            f1=f"{a}+{b}j"
            f2=f"{c}+{d}j"
            # print(f1,f2)

            

           


            
            self.results=f"{f1},\n{f2}"
        
        except Exception as e :
            self.results="INPUT ERROR"

        self.res=Label(text=self.results)
        self.add_widget(self.res)

        
        
          

        
        


class MyApp(App):
    def build(self):
        
        return my_layout()


    


appli=MyApp()   

if __name__ == "__main__":
    appli.run()
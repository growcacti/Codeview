import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, f4):
        #setting title
        f4.title("Screen Locations")
        #setting window size
        f4.background="#f6f8f9"
        width=1920
        height=1080
        screenwidth = f4.winfo_screenwidth()
        screenheight = f4.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        f4.geometry(alignstr)
        f4.resizable(width=True, height=True)

        GLabel_1=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_1["font"] = ft
        GLabel_1["fg"] = "#000000"
        GLabel_1["justify"] = "center"
        GLabel_1["text"] = "X10Y10"
        GLabel_1.place(x=10,y=10,width=100,height=25)

        GLabel_2=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_2["font"] = ft
        GLabel_2["fg"] = "#000000"
        GLabel_2["justify"] = "center"
        GLabel_2["text"] = "X100Y100"
        GLabel_2.place(x=100,y=100,width=100,height=25)

        GLabel_3=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_3["font"] = ft
        GLabel_3["fg"] = "#000000"
        GLabel_3["justify"] = "center"
        GLabel_3["text"] = "X200Y200"
        GLabel_3.place(x=200,y=200,width=100,height=25)

        GLabel_4=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_4["font"] = ft
        GLabel_4["fg"] = "#000000"
        GLabel_4["justify"] = "center"
        GLabel_4["text"] = "X500Y500"
        GLabel_4.place(x=500,y=500,width=100,height=25)

        GLabel_5=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_5["font"] = ft
        GLabel_5["fg"] = "#000000"
        GLabel_5["justify"] = "center"
        GLabel_5["text"] = "X750Y750"
        GLabel_5.place(x=750,y=750,width=100,height=25)

        GLabel_6=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_6["font"] = ft
        GLabel_6["fg"] = "#000000"
        GLabel_6["justify"] = "center"
        GLabel_6["text"] = "X1K_Y1K"
        GLabel_6.place(x=1000,y=1000,width=100,height=25)

        GLabel_7=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_7["font"] = ft
        GLabel_7["fg"] = "#000000"
        GLabel_7["justify"] = "center"
        GLabel_7["text"] = "X1.7k Y1.7k"
        GLabel_7.place(x=1700,y=1700,width=100,height=25)

        GLabel_8=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_8["font"] = ft
        GLabel_8["fg"] = "#000000"
        GLabel_8["justify"] = "center"
        GLabel_8["text"] = "X1.8kY100"
        GLabel_8.place(x=1800,y=100,width=100,height=25)

        GLabel_9=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_9["font"] = ft
        GLabel_9["fg"] = "#000000"
        GLabel_9["justify"] = "center"
        GLabel_9["text"] = "X1.8kY500"
        GLabel_9.place(x=1800,y=500,width=100,height=25)

        GLabel_10=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_10["font"] = ft
        GLabel_10["fg"] = "#000000"
        GLabel_10["justify"] = "center"
        GLabel_10["text"] = "X1.8kY900"
        GLabel_10.place(x=1800,y=900,width=100,height=25)


        GLabel_11=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_11["font"] = ft
        GLabel_11["fg"] = "#000000"
        GLabel_11["justify"] = "center"
        GLabel_11["text"] = "X100Y500"
        GLabel_11.place(x=100,y=500,width=100,height=25)
        
        GLabel_12=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_12["font"] = ft
        GLabel_12["fg"] = "#000000"
        GLabel_12["justify"] = "center"
        GLabel_12["text"] = "X1.3k Y700"
        GLabel_12.place(x=1300,y=700,width=100,height=25)

        GLabel_13=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_13["font"] = ft
        GLabel_13["fg"] = "#000000"
        GLabel_13["justify"] = "center"
        GLabel_13["text"] = "X1.4kY100"
        GLabel_13.place(x=1400,y=100,width=100,height=25)

        GLabel_14=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_14["font"] = ft
        GLabel_14["fg"] = "#000000"
        GLabel_14["justify"] = "center"
        GLabel_14["text"] = "X1.5kY500"
        GLabel_14.place(x=1500,y=500,width=100,height=25)

        GLabel_15=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_15["font"] = ft
        GLabel_10["fg"] = "#000000"
        GLabel_15["justify"] = "center"
        GLabel_15["text"] = "X1.6kY900"
        GLabel_15.place(x=1600,y=900,width=100,height=25)


        GLabel_16=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_16["font"] = ft
        GLabel_16["fg"] = "#000000"
        GLabel_16["justify"] = "center"
        GLabel_16["text"] = "X600Y500"
        GLabel_16.place(x=600,y=500,width=100,height=25)

        GLabel_17=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_17["font"] = ft
        GLabel_17["fg"] = "#000000"
        GLabel_17["justify"] = "center"
        GLabel_17["text"] = "X300Y400"
        GLabel_17.place(x=300,y=400,width=100,height=25)


        GLabel_18=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_18["font"] = ft
        GLabel_18["fg"] = "#000000"
        GLabel_18["justify"] = "center"
        GLabel_18["text"] = "X200Y400"
        GLabel_18.place(x=200,y=400,width=100,height=25)

        GLabel_19=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_19["font"] = ft
        GLabel_19["fg"] = "#000000"
        GLabel_19["justify"] = "center"
        GLabel_19["text"] = "X200Y800"
        GLabel_19.place(x=200,y=800,width=100,height=25)

        GLabel_20=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_20["font"] = ft
        GLabel_20["fg"] = "#000000"
        GLabel_20["justify"] = "center"
        GLabel_20["text"] = "X50Y450"
        GLabel_20.place(x=50,y=450,width=100,height=25)

        GLabel_21=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_21["font"] = ft
        GLabel_21["fg"] = "#000000"
        GLabel_21["justify"] = "center"
        GLabel_21["text"] = "X50Y250"
        GLabel_21.place(x=50,y=250,width=100,height=25)

        GLabel_22=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_22["font"] = ft
        GLabel_22["fg"] = "#000000"
        GLabel_22["justify"] = "center"
        GLabel_22["text"] = "X50Y650"
        GLabel_22.place(x=50,y=650,width=100,height=25)

        GLabel_23=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_23["font"] = ft
        GLabel_23["fg"] = "#000000"
        GLabel_23["justify"] = "center"
        GLabel_23["text"] = "X100Y200"
        GLabel_23.place(x=100,y=200,width=100,height=25)

        GLabel_24=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_24["font"] = ft
        GLabel_24["fg"] = "#000000"
        GLabel_24["justify"] = "center"
        GLabel_24["text"] = "X100Y500"
        GLabel_24.place(x=100,y=500,width=100,height=25)

        GLabel_25=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_25["font"] = ft
        GLabel_25["fg"] = "#000000"
        GLabel_25["justify"] = "center"
        GLabel_25["text"] = "X100Y800"
        GLabel_25.place(x=100,y=800,width=100,height=25)

        GLabel_26=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_26["font"] = ft
        GLabel_26["fg"] = "#000000"
        GLabel_26["justify"] = "center"
        GLabel_26["text"] = "X100Y900"
        GLabel_26.place(x=100,y=900,width=100,height=25)
         

        GLabel_27=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_27["font"] = ft
        GLabel_27["fg"] = "#000000"
        GLabel_27["justify"] = "center"
        GLabel_27["text"] = "X200Y900"
        GLabel_27.place(x=200,y=900,width=100,height=25)

        GLabel_28=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_28["font"] = ft
        GLabel_28["fg"] = "#000000"
        GLabel_28["justify"] = "center"
        GLabel_28["text"] = "X300Y900"
        GLabel_28.place(x=300,y=900,width=100,height=25)

        GLabel_29=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_29["font"] = ft
        GLabel_29["fg"] = "#000000"
        GLabel_29["justify"] = "center"
        GLabel_29["text"] = "X40Y40"
        GLabel_29.place(x=40,y=40,width=100,height=25)

        GLabel_30=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_30["font"] = ft
        GLabel_30["fg"] = "#000000"
        GLabel_30["justify"] = "center"
        GLabel_30["text"] = "X1.6kY800"
        GLabel_30.place(x=1600,y=800,width=100,height=25)


        GLabel_31=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_31["font"] = ft
        GLabel_31["fg"] = "#000000"
        GLabel_31["justify"] = "center"
        GLabel_31["text"] = "X150Y150"
        GLabel_31.place(x=150,y=150,width=100,height=25)

        GLabel_32=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_32["font"] = ft
        GLabel_32["fg"] = "#000000"
        GLabel_32["justify"] = "center"
        GLabel_32["text"] = "X325Y325"
        GLabel_32.place(x=325,y=325,width=100,height=25)


        GLabel_33=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_33["font"] = ft
        GLabel_33["fg"] = "#000000"
        GLabel_33["justify"] = "center"
        GLabel_33["text"] = "X475Y475"
        GLabel_33.place(x=475,y=475,width=100,height=25)

        GLabel_34=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_34["font"] = ft
        GLabel_34["fg"] = "#000000"
        GLabel_34["justify"] = "center"
        GLabel_34["text"] = "X475Y850"
        GLabel_34.place(x=475,y=850,width=100,height=25)

        GLabel_35=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_35["font"] = ft
        GLabel_35["fg"] = "#000000"
        GLabel_35["justify"] = "center"
        GLabel_35["text"] = "X125Y125"
        GLabel_35.place(x=125,y=125,width=100,height=25)

        GLabel_36=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_36["font"] = ft
        GLabel_36["fg"] = "#000000"
        GLabel_36["justify"] = "center"
        GLabel_36["text"] = "X950Y750"
        GLabel_36.place(x=950,y=750,width=100,height=25)

        GLabel_37=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_37["font"] = ft
        GLabel_37["fg"] = "#000000"
        GLabel_37["justify"] = "center"
        GLabel_37["text"] = "X850Y550"
        GLabel_37.place(x=850,y=550,width=100,height=25)

        GLabel_38=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_38["font"] = ft
        GLabel_38["fg"] = "#000000"
        GLabel_38["justify"] = "center"
        GLabel_38["text"] = "X750Y200"
        GLabel_38.place(x=750,y=200,width=100,height=25)

        GLabel_39=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_39["font"] = ft
        GLabel_39["fg"] = "#000000"
        GLabel_39["justify"] = "center"
        GLabel_39["text"] = "X600Y100"
        GLabel_39.place(x=600,y=100,width=100,height=25)

        GLabel_40=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_40["font"] = ft
        GLabel_40["fg"] = "#000000"
        GLabel_40["justify"] = "center"
        GLabel_40["text"] = "X600Y200"
        GLabel_40.place(x=600,y=200,width=100,height=25)

        GLabel_41=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_41["font"] = ft
        GLabel_41["fg"] = "#000000"
        GLabel_41["justify"] = "center"
        GLabel_41["text"] = "X600Y300"
        GLabel_41.place(x=600,y=300,width=100,height=25)

        
        GLabel_42=tk.Label(f4)
        ft = tkFont.Font(family='Ariel Black',size=10)
        GLabel_42["font"] = ft
        GLabel_42["fg"] = "#000000"
        GLabel_42["justify"] = "center"
        GLabel_42["text"] = "X300Y200"
        GLabel_42.place(x=300,y=200,width=100,height=25)
if __name__ == "__main__":
    f4 = tk.Tk()
    app = App(f4)
    f4.mainloop()


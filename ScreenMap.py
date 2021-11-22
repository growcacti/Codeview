import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(id_ego_superego, root):
        #setting title
        root.title("Screen Locations")
        #setting window size
        root.background="#f6f8f9"
        width=1920
        height=1080
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=True, height=True)

        GLabel_1=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_1["font"] = ft
        GLabel_1["fg"] = "#000000"
        GLabel_1["justify"] = "center"
        GLabel_1["text"] = "X10Y10"
        GLabel_1.place(x=10,y=10,width=100,height=25)

        GLabel_2=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_2["font"] = ft
        GLabel_2["fg"] = "#000000"
        GLabel_2["justify"] = "center"
        GLabel_2["text"] = "X100Y100"
        GLabel_2.place(x=100,y=100,width=100,height=25)

        GLabel_3=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_3["font"] = ft
        GLabel_3["fg"] = "#000000"
        GLabel_3["justify"] = "center"
        GLabel_3["text"] = "X200Y200"
        GLabel_3.place(x=200,y=200,width=100,height=25)

        GLabel_4=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_4["font"] = ft
        GLabel_4["fg"] = "#000000"
        GLabel_4["justify"] = "center"
        GLabel_4["text"] = "X500Y500"
        GLabel_4.place(x=500,y=500,width=100,height=25)

        GLabel_5=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5["font"] = ft
        GLabel_5["fg"] = "#000000"
        GLabel_5["justify"] = "center"
        GLabel_5["text"] = "X750Y750"
        GLabel_5.place(x=750,y=750,width=100,height=25)

        GLabel_6=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6["font"] = ft
        GLabel_6["fg"] = "#000000"
        GLabel_6["justify"] = "center"
        GLabel_6["text"] = "X1K_Y1K"
        GLabel_6.place(x=1000,y=1000,width=100,height=25)

        GLabel_7=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_7["font"] = ft
        GLabel_7["fg"] = "#000000"
        GLabel_7["justify"] = "center"
        GLabel_7["text"] = "X200Y400k"
        GLabel_7.place(x=200,y=400,width=100,height=25)

        GLabel_8=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_8["font"] = ft
        GLabel_8["fg"] = "#000000"
        GLabel_8["justify"] = "center"
        GLabel_8["text"] = "X300kY500"
        GLabel_8.place(x=300,y=500,width=100,height=25)

        GLabel_9=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_9["font"] = ft
        GLabel_9["fg"] = "#000000"
        GLabel_9["justify"] = "center"
        GLabel_9["text"] = "X600Y500"
        GLabel_9.place(x=600,y=500,width=100,height=25)

        GLabel_10=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_10["font"] = ft
        GLabel_10["fg"] = "#000000"
        GLabel_10["justify"] = "center"
        GLabel_10["text"] = "X1.8kY900"
        GLabel_10.place(x=1800,y=900,width=100,height=25)


        GLabel_11=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_11["font"] = ft
        GLabel_11["fg"] = "#000000"
        GLabel_11["justify"] = "center"
        GLabel_11["text"] = "X1.7KY400"
        GLabel_11.place(x=1700,y=400,width=100,height=25)
        
        GLabel_12=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_12["font"] = ft
        GLabel_12["fg"] = "#000000"
        GLabel_12["justify"] = "center"
        GLabel_12["text"] = "X1620Y700"
        GLabel_12.place(x=1620,y=700,width=150,height=50)

        GLabel_13=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_13["font"] = ft
        GLabel_13["fg"] = "#000000"
        GLabel_13["justify"] = "center"
        GLabel_13["text"] = "X1.4kY100"
        GLabel_13.place(x=1400,y=100,width=100,height=25)

        GLabel_14=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_14["font"] = ft
        GLabel_14["fg"] = "#000000"
        GLabel_14["justify"] = "center"
        GLabel_14["text"] = "X1.5kY500"
        GLabel_14.place(x=1500,y=500,width=100,height=25)

        GLabel_15=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_15["font"] = ft
        GLabel_10["fg"] = "#000000"
        GLabel_15["justify"] = "center"
        GLabel_15["text"] = "X1.6kY900"
        GLabel_15.place(x=1600,y=900,width=100,height=25)


        GLabel_16=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_16["font"] = ft
        GLabel_16["fg"] = "#000000"
        GLabel_16["justify"] = "center"
        GLabel_16["text"] = "X1.1KY500"
        GLabel_16.place(x=1100,y=500,width=100,height=25)

        GLabel_17=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_17["font"] = ft
        GLabel_17["fg"] = "#000000"
        GLabel_17["justify"] = "center"
        GLabel_17["text"] = "X1.3KY400"
        GLabel_17.place(x=1300,y=400,width=100,height=25)


        GLabel_18=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_18["font"] = ft
        GLabel_18["fg"] = "#000000"
        GLabel_18["justify"] = "center"
        GLabel_18["text"] = "X1.2Y400"
        GLabel_18.place(x=1200,y=400,width=100,height=25)

        GLabel_19=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_19["font"] = ft
        GLabel_19["fg"] = "#000000"
        GLabel_19["justify"] = "center"
        GLabel_19["text"] = "X1.2KY800"
        GLabel_19.place(x=1200,y=800,width=100,height=25)

        GLabel_20=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_20["font"] = ft
        GLabel_20["fg"] = "#000000"
        GLabel_20["justify"] = "center"
        GLabel_20["text"] = "X50Y450"
        GLabel_20.place(x=50,y=450,width=100,height=25)

        GLabel_21=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_21["font"] = ft
        GLabel_21["fg"] = "#000000"
        GLabel_21["justify"] = "center"
        GLabel_21["text"] = "X50Y250"
        GLabel_21.place(x=50,y=250,width=100,height=25)

        GLabel_22=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_22["font"] = ft
        GLabel_22["fg"] = "#000000"
        GLabel_22["justify"] = "center"
        GLabel_22["text"] = "X50Y650"
        GLabel_22.place(x=50,y=650,width=100,height=25)

        GLabel_23=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_23["font"] = ft
        GLabel_23["fg"] = "#000000"
        GLabel_23["justify"] = "center"
        GLabel_23["text"] = "X300Y200"
        GLabel_23.place(x=300,y=200,width=100,height=25)

        GLabel_24=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_24["font"] = ft
        GLabel_24["fg"] = "#000000"
        GLabel_24["justify"] = "center"
        GLabel_24["text"] = "X100Y500"
        GLabel_24.place(x=100,y=500,width=100,height=25)

        GLabel_25=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_25["font"] = ft
        GLabel_25["fg"] = "#000000"
        GLabel_25["justify"] = "center"
        GLabel_25["text"] = "X100Y800"
        GLabel_25.place(x=100,y=800,width=100,height=25)

        GLabel_26=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_26["font"] = ft
        GLabel_26["fg"] = "#000000"
        GLabel_26["justify"] = "center"
        GLabel_26["text"] = "X100Y900"
        GLabel_26.place(x=100,y=900,width=100,height=25)
         

        GLabel_27=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_27["font"] = ft
        GLabel_27["fg"] = "#000000"
        GLabel_27["justify"] = "center"
        GLabel_27["text"] = "X200Y900"
        GLabel_27.place(x=200,y=900,width=100,height=25)

        GLabel_28=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_28["font"] = ft
        GLabel_28["fg"] = "#000000"
        GLabel_28["justify"] = "center"
        GLabel_28["text"] = "X300Y900"
        GLabel_28.place(x=300,y=900,width=100,height=25)

        GLabel_29=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_29["font"] = ft
        GLabel_29["fg"] = "#000000"
        GLabel_29["justify"] = "center"
        GLabel_29["text"] = "X40Y40"
        GLabel_29.place(x=40,y=40,width=100,height=25)

        GLabel_30=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_30["font"] = ft
        GLabel_30["fg"] = "#000000"
        GLabel_30["justify"] = "center"
        GLabel_30["text"] = "X400Y800"
        GLabel_30.place(x=400,y=800,width=100,height=25)


        GLabel_31=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_31["font"] = ft
        GLabel_31["fg"] = "#000000"
        GLabel_31["justify"] = "center"
        GLabel_31["text"] = "X400Y150"
        GLabel_31.place(x=400,y=150,width=100,height=25)

        GLabel_32=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_32["font"] = ft
        GLabel_32["fg"] = "#000000"
        GLabel_32["justify"] = "center"
        GLabel_32["text"] = "X325Y325"
        GLabel_32.place(x=325,y=325,width=100,height=25)


        GLabel_33=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_33["font"] = ft
        GLabel_33["fg"] = "#000000"
        GLabel_33["justify"] = "center"
        GLabel_33["text"] = "X475Y475"
        GLabel_33.place(x=475,y=475,width=100,height=25)

        GLabel_34=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_34["font"] = ft
        GLabel_34["fg"] = "#000000"
        GLabel_34["justify"] = "center"
        GLabel_34["text"] = "X475Y850"
        GLabel_34.place(x=475,y=850,width=100,height=25)

        GLabel_35=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_35["font"] = ft
        GLabel_35["fg"] = "#000000"
        GLabel_35["justify"] = "center"
        GLabel_35["text"] = "X675Y475"
        GLabel_35.place(x=675,y=475,width=100,height=25)

        GLabel_36=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_36["font"] = ft
        GLabel_36["fg"] = "#000000"
        GLabel_36["justify"] = "center"
        GLabel_36["text"] = "X950Y750"
        GLabel_36.place(x=950,y=750,width=100,height=25)

        GLabel_37=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_37["font"] = ft
        GLabel_37["fg"] = "#000000"
        GLabel_37["justify"] = "center"
        GLabel_37["text"] = "X850Y550"
        GLabel_37.place(x=850,y=550,width=100,height=25)

        GLabel_38=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_38["font"] = ft
        GLabel_38["fg"] = "#000000"
        GLabel_38["justify"] = "center"
        GLabel_38["text"] = "X750Y200"
        GLabel_38.place(x=750,y=200,width=100,height=25)

        GLabel_39=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_39["font"] = ft
        GLabel_39["fg"] = "#000000"
        GLabel_39["justify"] = "center"
        GLabel_39["text"] = "X100Y600"
        GLabel_39.place(x=100,y=600,width=100,height=25)

        GLabel_40=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_40["font"] = ft
        GLabel_40["fg"] = "#000000"
        GLabel_40["justify"] = "center"
        GLabel_40["text"] = "X200Y600"
        GLabel_40.place(x=200,y=600,width=100,height=25)

        GLabel_41=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_41["font"] = ft
        GLabel_41["fg"] = "#000000"
        GLabel_41["justify"] = "center"
        GLabel_41["text"] = "X300Y600"
        GLabel_41.place(x=300,y=600,width=100,height=25)

        
        GLabel_42=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_42["font"] = ft
        GLabel_42["fg"] = "#000000"
        GLabel_42["justify"] = "center"
        GLabel_42["text"] = "X400Y600"
        GLabel_42.place(x=400,y=600,width=100,height=25)

        GLabel_43=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_43["font"] = ft
        GLabel_43["fg"] = "#000000"
        GLabel_43["justify"] = "center"
        GLabel_43["text"] = "X1250Y555"
        GLabel_43.place(x=1250,y=555,width=100,height=25)

        GLabel_44=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_44["font"] = ft
        GLabel_44["fg"] = "#000000"
        GLabel_44["justify"] = "center"
        GLabel_44["text"] = "X1.3kY400"
        GLabel_44.place(x=1300,y=400,width=100,height=25)

        GLabel_45=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_45["font"] = ft
        GLabel_45["fg"] = "#000000"
        GLabel_45["justify"] = "center"
        GLabel_45["text"] = "X1.3kY900"
        GLabel_45.place(x=1300,y=900,width=100,height=25)

        GLabel_46=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_46["font"] = ft
        GLabel_46["fg"] = "#000000"
        GLabel_46["justify"] = "center"
        GLabel_46["text"] = "X1.1kY350"
        GLabel_46.place(x=1100,y=350,width=100,height=25)

        GLabel_47=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_47["font"] = ft
        GLabel_47["fg"] = "#000000"
        GLabel_47["justify"] = "center"
        GLabel_47["text"] = "X1.1kY1k"
        GLabel_47.place(x=1100,y=1000,width=100,height=25)

        GLabel_48=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_48["font"] = ft
        GLabel_48["fg"] = "#000000"
        GLabel_48["justify"] = "center"
        GLabel_48["text"] = "X1.5kY320"
        GLabel_48.place(x=1500,y=320,width=100,height=25)

        GLabel_49=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_49["font"] = ft
        GLabel_49["fg"] = "#000000"
        GLabel_49["justify"] = "center"
        GLabel_49["text"] = "X1.6kY575"
        GLabel_49.place(x=1600,y=575,width=100,height=25)

        
        GLabel_50=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_50["font"] = ft
        GLabel_50["fg"] = "#000000"
        GLabel_50["justify"] = "center"
        GLabel_50["text"] = "X300Y200"
        GLabel_50.place(x=300,y=200,width=100,height=25)


        GLabel_550=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_550["font"] = ft
        GLabel_550["fg"] = "#000000"
        GLabel_550["justify"] = "center"
        GLabel_550["text"] = "X800Y300"
        GLabel_550.place(x=800,y=300,width=100,height=25)
                         
        GLabel_551=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_551["font"] = ft
        GLabel_551["fg"] = "#000000"
        GLabel_551["justify"] = "center"
        GLabel_551["text"] = "X900Y300"
        GLabel_551.place(x=900,y=300,width=100,height=25)

        GLabel_552=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_552["font"] = ft
        GLabel_552["fg"] = "#000000"
        GLabel_552["justify"] = "center"
        GLabel_552["text"] = "X1KY300"
        GLabel_552.place(x=1000,y=300,width=100,height=25)

        GLabel_553=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_553["font"] = ft
        GLabel_553["fg"] = "#000000"
        GLabel_553["justify"] = "center"
        GLabel_553["text"] = "X630Y430"
        GLabel_553.place(x=630,y=430,width=100,height=25)

        GLabel_554=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_554["font"] = ft
        GLabel_554["fg"] = "#000000"
        GLabel_554["justify"] = "center"
        GLabel_554["text"] = "X1560Y500"
        GLabel_554.place(x=1560,y=500,width=100,height=25)

        GLabel_55=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_55["font"] = ft
        GLabel_55["fg"] = "#000000"
        GLabel_55["justify"] = "center"
        GLabel_55["text"] = "X1750Y750"
        GLabel_55.place(x=1750,y=750,width=100,height=25)

        GLabel_60=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_60["font"] = ft
        GLabel_60["fg"] = "#000000"
        GLabel_60["justify"] = "center"
        GLabel_60["text"] = "X1K_Y20"
        GLabel_60.place(x=1000,y=20,width=100,height=25)

        GLabel_70=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_70["font"] = ft
        GLabel_70["fg"] = "#000000"
        GLabel_70["justify"] = "center"
        GLabel_70["text"] = "X900Y60"
        GLabel_70.place(x=900,y=60,width=100,height=25)

        GLabel_80=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_80["font"] = ft
        GLabel_80["fg"] = "#000000"
        GLabel_80["justify"] = "center"
        GLabel_80["text"] = "X1.8kY175"
        GLabel_80.place(x=1800,y=175,width=100,height=25)

        GLabel_92=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_92["font"] = ft
        GLabel_92["fg"] = "#000000"
        GLabel_92["justify"] = "center"
        GLabel_92["text"] = "X1.1kY50"
        GLabel_92.place(x=1100,y=50,width=100,height=25)

        GLabel_5510=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5510["font"] = ft
        GLabel_5510["fg"] = "#000000"
        GLabel_5510["justify"] = "center"
        GLabel_5510["text"] = "X1.8kY90"
        GLabel_5510.place(x=1600,y=300,width=100,height=25)


        GLabel_5511=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5511["font"] = ft
        GLabel_5511["fg"] = "#000000"
        GLabel_5511["justify"] = "center"
        GLabel_5511["text"] = "X1120Y150"
        GLabel_5511.place(x=1120,y=150,width=150,height=25)
        
        GLabel_5512=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5512["font"] = ft
        GLabel_5512["fg"] = "#000000"
        GLabel_5512["justify"] = "center"
        GLabel_5512["text"] = "X600Y700"
        GLabel_5512.place(x=600,y=700,width=100,height=25)

        GLabel_5513=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5513["font"] = ft
        GLabel_5513["fg"] = "#000000"
        GLabel_5513["justify"] = "center"
        GLabel_5513["text"] = "X700Y600"
        GLabel_5513.place(x=700,y=600,width=100,height=25)

        GLabel_5514=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5514["font"] = ft
        GLabel_5514["fg"] = "#000000"
        GLabel_5514["justify"] = "center"
        GLabel_5514["text"] = "X1560Y850"
        GLabel_5514.place(x=1560,y=850,width=150,height=25)

        GLabel_5515=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5515["font"] = ft
        GLabel_5510["fg"] = "#000000"
        GLabel_5515["justify"] = "center"
        GLabel_5515["text"] = "X800kY800"
        GLabel_5515.place(x=800,y=800,width=100,height=25)


        GLabel_5516=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5516["font"] = ft
        GLabel_5516["fg"] = "#000000"
        GLabel_5516["justify"] = "center"
        GLabel_5516["text"] = "X700Y700"
        GLabel_5516.place(x=700,y=700,width=100,height=25)

        GLabel_5517=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5517["font"] = ft
        GLabel_5517["fg"] = "#000000"
        GLabel_5517["justify"] = "center"
        GLabel_5517["text"] = "X600Y600"
        GLabel_5517.place(x=600,y=600,width=100,height=25)


        GLabel_5518=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5518["font"] = ft
        GLabel_5518["fg"] = "#000000"
        GLabel_5518["justify"] = "center"
        GLabel_5518["text"] = "X250Y400"
        GLabel_5518.place(x=250,y=400,width=100,height=25)

        GLabel_5519=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5519["font"] = ft
        GLabel_5519["fg"] = "#000000"
        GLabel_5519["justify"] = "center"
        GLabel_5519["text"] = "X350Y800"
        GLabel_5519.place(x=350,y=800,width=100,height=25)

        GLabel_5520=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5520["font"] = ft
        GLabel_5520["fg"] = "#000000"
        GLabel_5520["justify"] = "center"
        GLabel_5520["text"] = "X550Y250"
        GLabel_5520.place(x=550,y=250,width=100,height=25)

        GLabel_5521=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5521["font"] = ft
        GLabel_5521["fg"] = "#000000"
        GLabel_5521["justify"] = "center"
        GLabel_5521["text"] = "X650Y250"
        GLabel_5521.place(x=650,y=250,width=100,height=25)

        GLabel_5522=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5522["font"] = ft
        GLabel_5522["fg"] = "#000000"
        GLabel_5522["justify"] = "center"
        GLabel_5522["text"] = "X50Y650"
        GLabel_5522.place(x=950,y=350,width=100,height=25)

        GLabel_5523=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5523["font"] = ft
        GLabel_5523["fg"] = "#000000"
        GLabel_5523["justify"] = "center"
        GLabel_5523["text"] = "X1.2KY200"
        GLabel_5523.place(x=1200,y=200,width=100,height=25)

        GLabel_5524=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5524["font"] = ft
        GLabel_5524["fg"] = "#000000"
        GLabel_5524["justify"] = "center"
        GLabel_5524["text"] = "X1.3KY300"
        GLabel_5524.place(x=1300,y=300,width=100,height=25)

        GLabel_5525=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5525["font"] = ft
        GLabel_5525["fg"] = "#000000"
        GLabel_5525["justify"] = "center"
        GLabel_5525["text"] = "X1.1KY800"
        GLabel_5525.place(x=1100,y=800,width=100,height=25)

        GLabel_5526=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5526["font"] = ft
        GLabel_5526["fg"] = "#000000"
        GLabel_5526["justify"] = "center"
        GLabel_5526["text"] = "X250Y900"
        GLabel_5526.place(x=250,y=900,width=100,height=25)
         

        GLabel_5527=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5527["font"] = ft
        GLabel_5527["fg"] = "#000000"
        GLabel_5527["justify"] = "center"
        GLabel_5527["text"] = "X300Y800"
        GLabel_5527.place(x=300,y=800,width=100,height=25)

        GLabel_5528=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5528["font"] = ft
        GLabel_5528["fg"] = "#000000"
        GLabel_5528["justify"] = "center"
        GLabel_5528["text"] = "X1300Y90"
        GLabel_5528.place(x=1300,y=90,width=100,height=25)

        GLabel_5529=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5529["font"] = ft
        GLabel_5529["fg"] = "#000000"
        GLabel_5529["justify"] = "center"
        GLabel_5529["text"] = "X1440Y40"
        GLabel_5529.place(x=1440,y=40,width=100,height=25)

        GLabel_5530=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5530["font"] = ft
        GLabel_5530["fg"] = "#000000"
        GLabel_5530["justify"] = "center"
        GLabel_5530["text"] = "X1.6kY80"
        GLabel_5530.place(x=1600,y=80,width=100,height=25)


        GLabel_5531=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5531["font"] = ft
        GLabel_5531["fg"] = "#000000"
        GLabel_5531["justify"] = "center"
        GLabel_5531["text"] = "X1500Y15"
        GLabel_5531.place(x=1500,y=15,width=100,height=25)

        GLabel_5532=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5532["font"] = ft
        GLabel_5532["fg"] = "#000000"
        GLabel_5532["justify"] = "center"
        GLabel_5532["text"] = "X1325Y325"
        GLabel_5532.place(x=1325,y=325,width=100,height=25)


        GLabel_5533=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5533["font"] = ft
        GLabel_5533["fg"] = "#000000"
        GLabel_5533["justify"] = "center"
        GLabel_5533["text"] = "X1475Y475"
        GLabel_5533.place(x=1475,y=475,width=100,height=25)

        GLabel_5534=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5534["font"] = ft
        GLabel_5534["fg"] = "#000000"
        GLabel_5534["justify"] = "center"
        GLabel_5534["text"] = "X1475Y850"
        GLabel_5534.place(x=1475,y=850,width=100,height=25)

        GLabel_5535=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5535["font"] = ft
        GLabel_5535["fg"] = "#000000"
        GLabel_5535["justify"] = "center"
        GLabel_5535["text"] = "X1125Y125"
        GLabel_5535.place(x=1125,y=125,width=100,height=25)

        GLabel_5536=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5536["font"] = ft
        GLabel_5536["fg"] = "#000000"
        GLabel_5536["justify"] = "center"
        GLabel_5536["text"] = "X1910Y750"
        GLabel_5536.place(x=1910,y=750,width=100,height=25)

        GLabel_5537=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5537["font"] = ft
        GLabel_5537["fg"] = "#000000"
        GLabel_5537["justify"] = "center"
        GLabel_5537["text"] = "X1850Y55"
        GLabel_5537.place(x=1850,y=55,width=100,height=25)

        GLabel_5538=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5538["font"] = ft
        GLabel_5538["fg"] = "#000000"
        GLabel_5538["justify"] = "center"
        GLabel_5538["text"] = "X1750Y200"
        GLabel_5538.place(x=1750,y=200,width=100,height=25)

        GLabel_5539=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5539["font"] = ft
        GLabel_5539["fg"] = "#000000"
        GLabel_5539["justify"] = "center"
        GLabel_5539["text"] = "X1660Y100"
        GLabel_5539.place(x=1660,y=100,width=150,height=25)

        GLabel_5540=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5540["font"] = ft
        GLabel_5540["fg"] = "#000000"
        GLabel_5540["justify"] = "center"
        GLabel_5540["text"] = "X1680Y460"
        GLabel_5540.place(x=1680,y=460,width=100,height=25)

        GLabel_5541=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5541["font"] = ft
        GLabel_5541["fg"] = "#000000"
        GLabel_5541["justify"] = "center"
        GLabel_5541["text"] = "X1410Y300"
        GLabel_5541.place(x=1410,y=300,width=100,height=25)

        
        GLabel_5542=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5542["font"] = ft
        GLabel_5542["fg"] = "#000000"
        GLabel_5542["justify"] = "center"
        GLabel_5542["text"] = "X1320Y240"
        GLabel_5542.place(x=1320,y=240,width=100,height=25)

        GLabel_5543=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5543["font"] = ft
        GLabel_5543["fg"] = "#000000"
        GLabel_5543["justify"] = "center"
        GLabel_5543["text"] = "X1250Y555"
        GLabel_5543.place(x=1250,y=555,width=100,height=25)

        GLabel_5544=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5544["font"] = ft
        GLabel_5544["fg"] = "#000000"
        GLabel_5544["justify"] = "center"
        GLabel_5544["text"] = "X1.3kY400"
        GLabel_5544.place(x=1300,y=400,width=100,height=25)

        GLabel_5545=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5545["font"] = ft
        GLabel_5545["fg"] = "#000000"
        GLabel_5545["justify"] = "center"
        GLabel_5545["text"] = "X1.3kY900"
        GLabel_5545.place(x=1300,y=900,width=100,height=25)

        GLabel_5546=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5546["font"] = ft
        GLabel_5546["fg"] = "#000000"
        GLabel_5546["justify"] = "center"
        GLabel_5546["text"] = "X1.1kY350"
        GLabel_5546.place(x=1100,y=350,width=100,height=25)

        GLabel_5547=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5547["font"] = ft
        GLabel_5547["fg"] = "#000000"
        GLabel_5547["justify"] = "center"
        GLabel_5547["text"] = "X1.1kY1k"
        GLabel_5547.place(x=1100,y=1000,width=100,height=25)

        GLabel_5548=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5548["font"] = ft
        GLabel_5548["fg"] = "#000000"
        GLabel_5548["justify"] = "center"
        GLabel_5548["text"] = "X1.5kY320"
        GLabel_5548.place(x=1500,y=320,width=100,height=25)

        GLabel_5549=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_5549["font"] = ft
        GLabel_5549["fg"] = "#000000"
        GLabel_5549["justify"] = "center"
        GLabel_5549["text"] = "X1.1kY575"
        GLabel_5549.place(x=1100,y=575,width=100,height=25)
#-------------------------------------------------------------
        GLabel_66=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_66["font"] = ft
        GLabel_66["fg"] = "#000000"
        GLabel_66["justify"] = "center"
        GLabel_66["text"] = "X750Y750"
        GLabel_66.place(x=750,y=750,width=100,height=25)




        GLabel_660=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_660["font"] = ft
        GLabel_660["fg"] = "#000000"
        GLabel_660["justify"] = "center"
        GLabel_660["text"] = "X300Y200"
        GLabel_660.place(x=300,y=200,width=100, height=25)
                         
        GLabel_661=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_661["font"] = ft
        GLabel_661["fg"] = "#000000"
        GLabel_661["justify"] = "center"
        GLabel_661["text"] = "X10Y10"
        GLabel_661.place(x=10,y=10,width=100,height=25)

        GLabel_662=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_662["font"] = ft
        GLabel_662["fg"] = "#000000"
        GLabel_662["justify"] = "center"
        GLabel_662["text"] = "X100Y100"
        GLabel_662.place(x=100,y=100,width=100,height=25)

        GLabel_663=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_663["font"] = ft
        GLabel_663["fg"] = "#000000"
        GLabel_663["justify"] = "center"
        GLabel_663["text"] = "X200Y200"
        GLabel_663.place(x=200,y=200,width=100,height=25)

        GLabel_664=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_664["font"] = ft
        GLabel_664["fg"] = "#000000"
        GLabel_664["justify"] = "center"
        GLabel_664["text"] = "X500Y500"
        GLabel_664.place(x=500,y=500,width=100,height=25)

                    
        GLabel_6610=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6610["font"] = ft
        GLabel_6610["fg"] = "#000000"
        GLabel_6610["justify"] = "center"
        GLabel_6610["text"] = "X1.8kY900"
        GLabel_6610.place(x=1800,y=900,width=100,height=25)


        GLabel_6611=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6611["font"] = ft
        GLabel_6611["fg"] = "#000000"
        GLabel_6611["justify"] = "center"
        GLabel_6611["text"] = "X100Y500"
        GLabel_6611.place(x=100,y=500,width=100,height=25)
        
        GLabel_6612=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6612["font"] = ft
        GLabel_6612["fg"] = "#000000"
        GLabel_6612["justify"] = "center"
        GLabel_6612["text"] = "X1.3k Y700"
        GLabel_6612.place(x=1300,y=700,width=100,height=25)

        GLabel_6613=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6613["font"] = ft
        GLabel_6613["fg"] = "#000000"
        GLabel_6613["justify"] = "center"
        GLabel_6613["text"] = "X1.4kY100"
        GLabel_6613.place(x=1400,y=100,width=100,height=25)

        GLabel_6614=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6614["font"] = ft
        GLabel_6614["fg"] = "#000000"
        GLabel_6614["justify"] = "center"
        GLabel_6614["text"] = "X1.5kY500"
        GLabel_6614.place(x=1500,y=500,width=100,height=25)

        GLabel_6615=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6615["font"] = ft
        GLabel_6610["fg"] = "#000000"
        GLabel_6615["justify"] = "center"
        GLabel_6615["text"] = "X1.5kY900"
        GLabel_6615.place(x=1500,y=900,width=100,height=25)


        GLabel_6616=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6616["font"] = ft
        GLabel_6616["fg"] = "#000000"
        GLabel_6616["justify"] = "center"
        GLabel_6616["text"] = "X600Y500"
        GLabel_6616.place(x=600,y=500,width=100,height=25)

        GLabel_6617=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6617["font"] = ft
        GLabel_6617["fg"] = "#000000"
        GLabel_6617["justify"] = "center"
        GLabel_6617["text"] = "X300Y400"
        GLabel_6617.place(x=300,y=400,width=100,height=25)


        GLabel_6618=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6618["font"] = ft
        GLabel_6618["fg"] = "#000000"
        GLabel_6618["justify"] = "center"
        GLabel_6618["text"] = "X200Y400"
        GLabel_6618.place(x=200,y=400,width=100,height=25)

        GLabel_6619=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6619["font"] = ft
        GLabel_6619["fg"] = "#000000"
        GLabel_6619["justify"] = "center"
        GLabel_6619["text"] = "X200Y800"
        GLabel_6619.place(x=200,y=800,width=100,height=25)

        GLabel_6620=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6620["font"] = ft
        GLabel_6620["fg"] = "#000000"
        GLabel_6620["justify"] = "center"
        GLabel_6620["text"] = "X50Y450"
        GLabel_6620.place(x=50,y=450,width=100,height=25)

        GLabel_6621=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6621["font"] = ft
        GLabel_6621["fg"] = "#000000"
        GLabel_6621["justify"] = "center"
        GLabel_6621["text"] = "X50Y250"
        GLabel_6621.place(x=50,y=250,width=100,height=25)

        GLabel_6622=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6622["font"] = ft
        GLabel_6622["fg"] = "#000000"
        GLabel_6622["justify"] = "center"
        GLabel_6622["text"] = "X50Y650"
        GLabel_6622.place(x=50,y=650,width=100,height=25)

        GLabel_6623=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6623["font"] = ft
        GLabel_6623["fg"] = "#000000"
        GLabel_6623["justify"] = "center"
        GLabel_6623["text"] = "X100Y200"
        GLabel_6623.place(x=100,y=200,width=100,height=25)

        GLabel_6624=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6624["font"] = ft
        GLabel_6624["fg"] = "#000000"
        GLabel_6624["justify"] = "center"
        GLabel_6624["text"] = "X100Y500"
        GLabel_6624.place(x=100,y=500,width=100,height=25)

        GLabel_6625=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6625["font"] = ft
        GLabel_6625["fg"] = "#000000"
        GLabel_6625["justify"] = "center"
        GLabel_6625["text"] = "X100Y800"
        GLabel_6625.place(x=100,y=800,width=100,height=25)

        GLabel_6626=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6626["font"] = ft
        GLabel_6626["fg"] = "#000000"
        GLabel_6626["justify"] = "center"
        GLabel_6626["text"] = "X100Y900"
        GLabel_6626.place(x=100,y=900,width=100,height=25)
         

        GLabel_6627=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6627["font"] = ft
        GLabel_6627["fg"] = "#000000"
        GLabel_6627["justify"] = "center"
        GLabel_6627["text"] = "X200Y900"
        GLabel_6627.place(x=200,y=900,width=100,height=25)

        GLabel_6628=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6628["font"] = ft
        GLabel_6628["fg"] = "#000000"
        GLabel_6628["justify"] = "center"
        GLabel_6628["text"] = "X300Y900"
        GLabel_6628.place(x=300,y=900,width=100,height=25)

        GLabel_6629=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6629["font"] = ft
        GLabel_6629["fg"] = "#000000"
        GLabel_6629["justify"] = "center"
        GLabel_6629["text"] = "X40Y40"
        GLabel_6629.place(x=40,y=40,width=100,height=25)

        GLabel_6630=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6630["font"] = ft
        GLabel_6630["fg"] = "#000000"
        GLabel_6630["justify"] = "center"
        GLabel_6630["text"] = "X1.6kY800"
        GLabel_6630.place(x=1600,y=800,width=100,height=25)


        GLabel_6631=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6631["font"] = ft
        GLabel_6631["fg"] = "#000000"
        GLabel_6631["justify"] = "center"
        GLabel_6631["text"] = "X150Y150"
        GLabel_6631.place(x=150,y=150,width=100,height=25)

        GLabel_6632=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6632["font"] = ft
        GLabel_6632["fg"] = "#000000"
        GLabel_6632["justify"] = "center"
        GLabel_6632["text"] = "X325Y325"
        GLabel_6632.place(x=325,y=325,width=100,height=25)


        GLabel_6633=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6633["font"] = ft
        GLabel_6633["fg"] = "#000000"
        GLabel_6633["justify"] = "center"
        GLabel_6633["text"] = "X475Y475"
        GLabel_6633.place(x=475,y=475,width=100,height=25)

        GLabel_6634=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6634["font"] = ft
        GLabel_6634["fg"] = "#000000"
        GLabel_6634["justify"] = "center"
        GLabel_6634["text"] = "X475Y850"
        GLabel_6634.place(x=475,y=850,width=100,height=25)

        GLabel_6635=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6635["font"] = ft
        GLabel_6635["fg"] = "#000000"
        GLabel_6635["justify"] = "center"
        GLabel_6635["text"] = "X125Y125"
        GLabel_6635.place(x=125,y=125,width=100,height=25)

        GLabel_6636=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6636["font"] = ft
        GLabel_6636["fg"] = "#000000"
        GLabel_6636["justify"] = "center"
        GLabel_6636["text"] = "X950Y750"
        GLabel_6636.place(x=950,y=750,width=100,height=25)

        GLabel_6637=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6637["font"] = ft
        GLabel_6637["fg"] = "#000000"
        GLabel_6637["justify"] = "center"
        GLabel_6637["text"] = "X850Y550"
        GLabel_6637.place(x=850,y=550,width=100,height=25)

        GLabel_6638=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6638["font"] = ft
        GLabel_6638["fg"] = "#000000"
        GLabel_6638["justify"] = "center"
        GLabel_6638["text"] = "X750Y200"
        GLabel_6638.place(x=750,y=200,width=100,height=25)

        GLabel_6639=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6639["font"] = ft
        GLabel_6639["fg"] = "#000000"
        GLabel_6639["justify"] = "center"
        GLabel_6639["text"] = "X600Y100"
        GLabel_6639.place(x=600,y=100,width=100,height=25)

        GLabel_6640=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6640["font"] = ft
        GLabel_6640["fg"] = "#000000"
        GLabel_6640["justify"] = "center"
        GLabel_6640["text"] = "X600Y200"
        GLabel_6640.place(x=600,y=200,width=100,height=25)

        GLabel_6641=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6641["font"] = ft
        GLabel_6641["fg"] = "#000000"
        GLabel_6641["justify"] = "center"
        GLabel_6641["text"] = "X600Y300"
        GLabel_6641.place(x=600,y=300,width=100,height=25)

        
        GLabel_6642=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6642["font"] = ft
        GLabel_6642["fg"] = "#000000"
        GLabel_6642["justify"] = "center"
        GLabel_6642["text"] = "X1300Y270"
        GLabel_6642.place(x=1300,y=270,width=150,height=25)

        GLabel_6643=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6643["font"] = ft
        GLabel_6643["fg"] = "#000000"
        GLabel_6643["justify"] = "center"
        GLabel_6643["text"] = "X1250Y555"
        GLabel_6643.place(x=1250,y=555,width=100,height=25)

        GLabel_6644=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6644["font"] = ft
        GLabel_6644["fg"] = "#000000"
        GLabel_6644["justify"] = "center"
        GLabel_6644["text"] = "X1.3kY400"
        GLabel_6644.place(x=1300,y=400,width=100,height=25)

        GLabel_6645=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6645["font"] = ft
        GLabel_6645["fg"] = "#000000"
        GLabel_6645["justify"] = "center"
        GLabel_6645["text"] = "X1.3kY900"
        GLabel_6645.place(x=1300,y=900,width=100,height=25)

        GLabel_6646=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6646["font"] = ft
        GLabel_6646["fg"] = "#000000"
        GLabel_6646["justify"] = "center"
        GLabel_6646["text"] = "X1.1kY350"
        GLabel_6646.place(x=1100,y=350,width=100,height=25)

        GLabel_6647=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6647["font"] = ft
        GLabel_6647["fg"] = "#000000"
        GLabel_6647["justify"] = "center"
        GLabel_6647["text"] = "X1.1kY1k"
        GLabel_6647.place(x=1100,y=1000,width=100,height=25)

        GLabel_6648=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6648["font"] = ft
        GLabel_6648["fg"] = "#000000"
        GLabel_6648["justify"] = "center"
        GLabel_6648["text"] = "X1.5kY320"
        GLabel_6648.place(x=1500,y=320,width=100,height=25)

        GLabel_6649=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_6649["font"] = ft
        GLabel_6649["fg"] = "#000000"
        GLabel_6649["justify"] = "center"
        GLabel_6649["text"] = "X1260Y575"
        GLabel_6649.place(x=1260,y=575,width=100,height=25)

        
        GLabel_7739=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_7739["font"] = ft
        GLabel_7739["fg"] = "#000000"
        GLabel_7739["justify"] = "center"
        GLabel_7739["text"] = "X300Y100"
        GLabel_7739.place(x=300,y=100,width=100,height=25)

        GLabel_7740=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_7740["font"] = ft
        GLabel_7740["fg"] = "#000000"
        GLabel_7740["justify"] = "center"
        GLabel_7740["text"] = "X500Y100"
        GLabel_7740.place(x=500,y=100,width=100,height=25)

        GLabel_7741=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_7741["font"] = ft
        GLabel_7741["fg"] = "#000000"
        GLabel_7741["justify"] = "center"
        GLabel_7741["text"] = "X350Y250"
        GLabel_7741.place(x=350,y=250,width=100,height=25)

        
        GLabel_7742=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_7742["font"] = ft
        GLabel_7742["fg"] = "#000000"
        GLabel_7742["justify"] = "center"
        GLabel_7742["text"] = "X475Y400"
        GLabel_7742.place(x=475,y=400,width=150,height=25)

        GLabel_7743=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_7743["font"] = ft
        GLabel_7743["fg"] = "#000000"
        GLabel_7743["justify"] = "center"
        GLabel_7743["text"] = "X475Y350"
        GLabel_7743.place(x=475,y=350,width=100,height=25)

        GLabel_7744=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_7744["font"] = ft
        GLabel_7744["fg"] = "#000000"
        GLabel_7744["justify"] = "center"
        GLabel_7744["text"] = "X100Y700"
        GLabel_7744.place(x=100,y=700,width=100,height=25)

        GLabel_7745=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_7745["font"] = ft
        GLabel_7745["fg"] = "#000000"
        GLabel_7745["justify"] = "center"
        GLabel_7745["text"] = "X300Y700"
        GLabel_7745.place(x=300,y=700,width=100,height=25)

        GLabel_7746=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_7746["font"] = ft
        GLabel_7746["fg"] = "#000000"
        GLabel_7746["justify"] = "center"
        GLabel_7746["text"] = "X100Y1k"
        GLabel_7746.place(x=100,y=1000,width=100,height=25)

        GLabel_7747=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_7747["font"] = ft
        GLabel_7747["fg"] = "#000000"
        GLabel_7747["justify"] = "center"
        GLabel_7747["text"] = "X200Y1k"
        GLabel_7747.place(x=200,y=1000,width=100,height=25)

        GLabel_7748=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_7748["font"] = ft
        GLabel_7748["fg"] = "#000000"
        GLabel_7748["justify"] = "center"
        GLabel_7748["text"] = "X300Y1k"
        GLabel_7748.place(x=300,y=1000,width=100,height=25)

        GLabel_7749=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_7749["font"] = ft
        GLabel_7749["fg"] = "#000000"
        GLabel_7749["justify"] = "center"
        GLabel_7749["text"] = "X400Y1k"
        GLabel_7749.place(x=400,y=1000,width=100,height=25)

        GLabel_8839=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_8839["font"] = ft
        GLabel_8839["fg"] = "#000000"
        GLabel_8839["justify"] = "center"
        GLabel_8839["text"] = "X100Y900"
        GLabel_8839.place(x=100,y=900,width=100,height=25)

        GLabel_8840=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_8840["font"] = ft
        GLabel_8840["fg"] = "#000000"
        GLabel_8840["justify"] = "center"
        GLabel_8840["text"] = "X200Y900"
        GLabel_8840.place(x=200,y=900,width=100,height=25)

        GLabel_8841=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_8841["font"] = ft
        GLabel_8841["fg"] = "#000000"
        GLabel_8841["justify"] = "center"
        GLabel_8841["text"] = "X350Y900"
        GLabel_8841.place(x=350,y=900,width=100,height=25)

        
        GLabel_8842=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_8842["font"] = ft
        GLabel_8842["fg"] = "#000000"
        GLabel_8842["justify"] = "center"
        GLabel_8842["text"] = "X475Y900"
        GLabel_8842.place(x=475,y=900,width=150,height=25)

        GLabel_8843=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_8843["font"] = ft
        GLabel_8843["fg"] = "#000000"
        GLabel_8843["justify"] = "center"
        GLabel_8843["text"] = "X525Y900"
        GLabel_8843.place(x=525,y=900,width=100,height=25)

        GLabel_8844=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_8844["font"] = ft
        GLabel_8844["fg"] = "#000000"
        GLabel_8844["justify"] = "center"
        GLabel_8844["text"] = "X100Y800"
        GLabel_8844.place(x=100,y=800,width=100,height=25)

        GLabel_8845=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_8845["font"] = ft
        GLabel_8845["fg"] = "#000000"
        GLabel_8845["justify"] = "center"
        GLabel_8845["text"] = "X300Y800"
        GLabel_8845.place(x=300,y=800,width=100,height=25)

        GLabel_8846=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_8846["font"] = ft
        GLabel_8846["fg"] = "#000000"
        GLabel_8846["justify"] = "center"
        GLabel_8846["text"] = "X400Y800"
        GLabel_8846.place(x=400,y=800,width=100,height=25)

        GLabel_8847=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_8847["font"] = ft
        GLabel_8847["fg"] = "#000000"
        GLabel_8847["justify"] = "center"
        GLabel_8847["text"] = "X600Y800"
        GLabel_8847.place(x=600,y=800,width=100,height=25)

        GLabel_8848=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_8848["font"] = ft
        GLabel_8848["fg"] = "#000000"
        GLabel_8848["justify"] = "center"
        GLabel_8848["text"] = "X700Y800"
        GLabel_8848.place(x=700,y=800,width=100,height=25)

        GLabel_8849=tk.Label(root)
        ft = tkFont.Font(family='Ariel Black',size=8)
        GLabel_8849["font"] = ft
        GLabel_8849["fg"] = "#000000"
        GLabel_8849["justify"] = "center"
        GLabel_8849["text"] = "X480Y929"
        GLabel_8849.place(x=480,y=929,width=100,height=25)                


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

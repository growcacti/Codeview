import tkinter as tkinter
import tkinter.messagebox as mb
import random,time

class Ball():
    

    def __init__(self,canvas,paddle,score,color,init_x=100,init_y=100):
        
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.color = color

        self.id = canvas.create_oval(10,10,30,30,fill=self.color)
        self.canvas.move(self.id,init_x,init_y)

        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False


    def draw(self):
        
        self.canvas.move(self.id,self.x,self.y)
        position = self.canvas.coords(self.id)
        if position[1] <= 0:
            self.y = 3
        if position[3] >= self.canvas_height:  
            self.hit_bottom = True
        if self.hit_paddle(position) == True: 
            self.y = -3
        if position[0] <= 0: 
        if position[2] >= self.canvas_width: # 如果小球的右下角x坐标 大于等于画布宽度，则向左移动3个像素
            self.x = -3


    def hit_paddle(self,position):
        
        paddle_position = self.canvas.coords(self.paddle.id)
        print (,paddle_position[0],paddle_position[1],paddle_position[2],paddle_position[3])
        if position[2] >= paddle_position[0] and position[0] <= paddle_position[2]:
           if position[3] >= paddle_position[1] and position[3] <= paddle_position[3]:
               self.x += self.paddle.x
               colors = [,]
               random.shuffle(colors)
               self.color= colors[0]
               self.canvas.itemconfig(self.id,fill=colors[0])
               self.score.hit(ball_color = self.color)
               self.canvas.itemconfig(self.paddle.id,fill=self.color)
               self.adjust_paddle(paddle_position)
               return True

        return False


    def adjust_paddle(self,paddle_position):
        
        paddle_grow_length = 30
        paddle_width = paddle_position[2] - paddle_position[0]
        if self.color == : # 如果当前球的颜色为红色
            if paddle_width > 30: # 如果球拍的宽度大于60
                if paddle_position[2] >= self.canvas_width: # 如果球拍右下角的x坐标 大于等于 画布宽度
                    paddle_position[2] = paddle_position[2] - paddle_grow_length
                else:
                    paddle_position[0] = paddle_position[0] + paddle_grow_length

        elif self.color == : # 如果当前球的颜色为绿色
            if paddle_width < 300: # 如果球拍的宽度小于300
                if paddle_position[2] >= self.canvas_width: # 如果球拍的右下角x坐标 大于等于 画布宽度
                    paddle_position[0] = paddle_position[0] - paddle_grow_length
                else:
                    paddle_position[2]=paddle_position[2]+paddle_grow_length


class Paddle:
    
    def __init__(self,canvas,color):
        
        self.canvas = canvas
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.id = canvas.create_rectangle(0,0,180,15,fill=color)
        self.canvas.move(self.id,200,self.canvas_height*0.75)
        self.x = 0
        self.started = False
        self.continue_game = False
        self.canvas.bind_all(,self.turn_left)
        self.canvas.bind_all(,self.turn_right)
        self.canvas.bind_all(,self.continue_game)
        self.canvas.bind_all(,self.start_game)
        self.canvas.bind_all(,self.pause_game)

    def turn_left(self,event):
        
        position = self.canvas.coords(self.id)
        if position[0] <= 0:
            self.x = 0
        else:
            self.x = -3

    def turn_right(self,event):

        position = self.canvas.coords(self.id)
        if position[2] >= self.canvas_width:
            self.x = 0
        else:
            self.x = 3

    def start_game(self,evt):
        self.started = True

    def pause_game(self,evt):
        if self.started:
            self.started=False
        else:
            self.started=True

    def draw(self):
        
        self.canvas.move(self.id,self.x,0)
        position = self.canvas.coords(self.id)
        if position[0] <= 0:
            self.x = 0
        elif position[2] >= self.canvas_width:
            self.x = 0


class Score():
    
    def __init__(self,canvas,color):
        
        self.score = 0
        self.canvas = canvas
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.id = canvas.create_text(self.canvas_width-150,10,text=,fill=color,font=(None, 18, ))
        self.note = canvas.create_text(self.canvas_width-70,10,text=,fill=,font=(None, 18, ))

    def hit(self,ball_color=):
        grey
        self.score += 1
        self.canvas.itemconfig(self.id,text=.format(self.score))
        if ball_color == :
            self.canvas.itemconfig(self.note,text=.format(),fill=)
        elif ball_color==:
            self.canvas.itemconfig(self.note,text=.format(),fill=)
        else:
            self.canvas.itemconfig(self.note,text=,fill=)

def main():
    tk = tkinter.Tk()
    def callback():
        
        if mb.askokcancel(, ):
            tk.destroy()
    tk.protocol(, callback)

    canvas_width = 600
    canvas_hight = 500
    tk.title()
    tk.resizable(0,0)
    tk.wm_attributes(,1)
    canvas = tkinter.Canvas(tk,width=canvas_width,height=canvas_hight,bd=0,highlightthickness=0,bg=)
    canvas.pack()
    tk.update()

    score = Score(canvas,)
    paddle = Paddle(canvas,)
    ball = Ball(canvas,paddle,score,)

    game_over_text = canvas.create_text(canvas_width/2,canvas_hight/2,text=,state=,fill=,font=(None, 18, ))
    introduce = 
    game_start_text = canvas.create_text(canvas_width/2,canvas_hight/2,text=introduce,state=,fill=,font=(None, 18, ))

    while True:
        if (ball.hit_bottom == False) and ball.paddle.started:
            canvas.itemconfig(game_start_text,state=)
            ball.draw()
            paddle.draw()
        if ball.hit_bottom == True:
            time.sleep(0.1)
            canvas.itemconfig(game_over_text,state=)
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)

if __name__==:
    main()






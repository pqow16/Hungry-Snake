#!/usr/bin/env python
# coding: utf-8

# In[31]:


import tkinter as tk
from tkinter import messagebox
import random

#用python基本的GUI programming - tkinter寫出貪食蛇
class frm_main(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent=parent
        
    #主選單GUI設置
    def startmenu(self):
        self.frm_title=tk.Frame(master=self.parent, relief=tk.FLAT,bg='coral')
        self.lbl_title=tk.Label(
            master=self.frm_title,
            text='Hungry snake',
            foreground='green',
            background='coral')
        self.lbl_message=tk.Label(
            master=self.frm_title,
            text='Author: sunny333456',
            foreground='black',
            background='coral')
        self.frm_title.columnconfigure(0, weight=1, minsize=40)
        self.frm_title.rowconfigure(0, weight=1, minsize=40)
        self.lbl_title.grid(row=0, column=0, sticky='news')
        self.frm_title.rowconfigure(1, weight=1, minsize=40)
        self.lbl_message.grid(row=1, column=0, sticky='news')
        self.frm_title.grid(row=0, column=0, padx=30, pady=5, sticky='news')

        self.frm_player=tk.Frame(master=self.parent, relief=tk.FLAT, borderwidth=10)
        self.frm_bundle=tk.Frame(master=self.frm_player)
        self.lbl_playertitle=tk.Label(master=self.frm_bundle, text='Player name:')
        self.ent_player=tk.Entry(master=self.frm_bundle)
        self.frm_bundle.pack(side='bottom')
        self.lbl_playertitle.pack(side='left')
        self.ent_player.pack(side='left')
        self.frm_player.grid(row=1, column=0, padx=10, pady=10, sticky='news')

        self.frm_button=tk.Frame(master=self.parent)
        self.frm_button_start=tk.Frame(master=self.frm_button, relief=tk.RAISED)
        self.btn_start=tk.Button(
            master=self.frm_button_start,
            text='Start next round!',
            fg='black',
            bg='white',
            width=20,
            height=4,
            command=self.startgame)
        self.frm_button_guild=tk.Frame(master=self.frm_button, relief=tk.RAISED)
        self.btn_guild=tk.Button(
            master=self.frm_button_guild,
            text='How to play?',
            fg='black',
            bg='white',
            width=12,
            height=2,
            command=self.howToPlay)
        self.frm_button_start.pack(side=tk.TOP)
        self.frm_button_guild.pack(side=tk.BOTTOM)
        self.btn_start.pack()
        self.btn_guild.pack()
        self.frm_button.grid(row=2, column=0, padx=30, pady=5, sticky='news')
        
        self.delay=1000
        self.difficulty='Normal'
        self.difficulty_var=tk.StringVar()
        self.difficulty_var.set("Difficulty: {}".format(self.difficulty))
        self.frm_difficulty=tk.Frame(master=self.parent)
        self.lbl_difficulty=tk.Label(master=self.frm_difficulty, textvariable=self.difficulty_var)
        self.btn_easy=tk.Button(master=self.frm_difficulty, text='Easy', command=self.seteasy)
        self.btn_normal=tk.Button(master=self.frm_difficulty, text='Normal', command=self.setnormal)
        self.btn_hard=tk.Button(master=self.frm_difficulty, text='Hard', command=self.sethard)
        self.frm_difficulty.grid(row=3, column=0, padx=0, pady=5, sticky='news')
        self.lbl_difficulty.grid(row=0, column=1, padx=0, pady=1, sticky='news')
        self.btn_easy.grid(row=1, column=0, padx=1, pady=0, sticky='news')
        self.btn_normal.grid(row=1, column=1, padx=1, pady=0, sticky='news')
        self.btn_hard.grid(row=1, column=2, padx=1, pady=0, sticky='news')
        self.frm_difficulty.columnconfigure(0, weight=1, minsize=8)
        self.frm_difficulty.columnconfigure(1, weight=1, minsize=8)
        self.frm_difficulty.columnconfigure(2, weight=1, minsize=8)
        
        
    
    def startgame(self):
        self.playername=self.ent_player.get()
        self.obj_game=wdw_game(self.parent, self.playername, self.delay)
        self.obj_game.startgame()
    def howToPlay(self):
        tk.messagebox.showinfo(title='How to play?',
                               message='Use \'w\', \'a\', \'s\', \'d\' on keyboard to control snake. \
                               \nEat food(white grid) to gain score')
        
    def seteasy(self):
        self.delay=1500
        self.difficulty='Easy'
        self.difficulty_var.set("Difficulty: {}".format(self.difficulty))
        self.lbl_difficulty.update_idletasks()
    def setnormal(self):
        self.delay=1000
        self.difficulty='Normal'
        self.difficulty_var.set("Difficulty: {}".format(self.difficulty))
        self.lbl_difficulty.update_idletasks()
    def sethard(self):
        self.delay=500
        self.difficulty='Hard'
        self.difficulty_var.set("Difficulty: {}".format(self.difficulty))
        self.lbl_difficulty.update_idletasks()
        
#遊戲視窗
class wdw_game(tk.Toplevel):
    def __init__(self, parent, playername, delay):
        tk.Toplevel.__init__(self, parent)
        self.parent=parent
        self.playername=playername
        self.delay=delay
    
    #開始遊戲
    def startgame(self):
        #遊戲GUI設置
        self.frm_info=tk.Frame(master=self)
        self.lbl_player=tk.Label(master=self.frm_info, text=['Player:',self.playername])
        self.score=0
        self.score_var=tk.IntVar()
        self.score_var.set("   Your score: {}".format(self.score))
        self.lbl_score=tk.Label(master=self.frm_info, textvariable=self.score_var)
        self.lbl_player.pack(side=tk.LEFT)
        self.lbl_score.pack(side=tk.LEFT)
        self.rowconfigure(0, weight=1, minsize=80)
        self.columnconfigure(0, weight=1, minsize=80)
        self.frm_info.grid(row=0, column=0, padx=10, pady=10, sticky='news')

        self.frm_game_main=tk.Frame(master=self)
        self.rowconfigure(1, weight=1, minsize=420)
        self.columnconfigure(0, weight=1, minsize=210)
        self.frm_game_main.grid(row=1, column=0, padx=20, pady=10, sticky='news')
        
        #遊戲畫面設置
        #先畫出 column x row個格子
        self.row=11
        self.column=11
        self.non_occupied={}
        for i in range(self.row):
            for j in range(self.column):
                self.non_occupied[i,j]=None
                self.frm_game_main.rowconfigure(i, minsize=10)
                self.frm_game_main.columnconfigure(j, minsize=10)
                self.lbl_game_grid=tk.Label(master=self.frm_game_main, width=4, height=2, bg='black')
                self.lbl_game_grid.grid(row=i, column=j, padx=1, pady=1)
        
        #初始化蛇的位置。occupied代表蛇的位置，non_occupied代表剩餘空間
        #創造一個長度為3，頭朝+Y方向的蛇
        self.occupied=[[5,5],[5,4],[5,3]]
        del self.non_occupied[5,5]
        del self.non_occupied[5,4]
        del self.non_occupied[5,3]
        self.lbl_game_grid=tk.Label(master=self.frm_game_main, width=4, height=2, bg='red')
        self.lbl_game_grid.grid(row=(self.row-1-5), column=5, padx=1, pady=1)#因為row的方向與y的方向相反，操作上要注意
        self.lbl_game_grid=tk.Label(master=self.frm_game_main, width=4, height=2, bg='green')
        self.lbl_game_grid.grid(row=(self.row-1-4), column=5, padx=1, pady=1)
        self.lbl_game_grid=tk.Label(master=self.frm_game_main, width=4, height=2, bg='green')
        self.lbl_game_grid.grid(row=(self.row-1-3), column=5, padx=1, pady=1)
        
        #食物
        self.food=(7,7)
        self.lbl_game_grid=tk.Label(master=self.frm_game_main, width=4, height=2, bg='white')
        self.lbl_game_grid.grid(row=(self.row-1-self.food[1]), column=self.food[0], padx=1, pady=1)
        
        #遊戲初始化
        self.bind(("<Key>"), self.validate)
        self.direction='w'
        self.gameover=False
        self.runnn()
        
    #讓遊戲持續循環的method
    def runnn(self):
        self.occupied.insert(0, self.heading(self.occupied[0], self.direction)) #新增頭

        #畫圖
        if self.gameover==False:
            self.lbl_game_grid=tk.Label(master=self.frm_game_main, width=4, height=2, bg='red')
            self.lbl_game_grid.grid(row=(self.row-1-self.occupied[0][1]), 
                                    column=self.occupied[0][0], padx=1, pady=1)
            self.lbl_game_grid=tk.Label(master=self.frm_game_main, width=4, height=2, bg='green')
            self.lbl_game_grid.grid(row=(self.row-1-self.occupied[1][1]), 
                                    column=self.occupied[1][0], padx=1, pady=1)
        #Game over
        else:
            if messagebox.askyesno(title='Game Over!!!', message='Play again?'):
                self.destroy()
                return
            else:
                self.destroy()
                self.parent.destroy()
                return

        self.after(self.delay, self.runnn)

    
    #蛇的移動
    def heading(self, head, direction):
        #先移除屁股
        self.oldbutt=self.occupied[-1]
        self.lbl_game_grid=tk.Label(master=self.frm_game_main, width=4, height=2, bg='black')
        self.lbl_game_grid.grid(row=(self.row-1-self.oldbutt[1]), 
                                column=self.oldbutt[0], padx=1, pady=1)
        self.non_occupied[tuple(self.occupied.pop(-1))]=None
        #開始處理頭
        if direction=='w' or direction=='W':
            newhead=(head[0], head[1]+1)
            if newhead in self.non_occupied:
                del self.non_occupied[newhead]
                if newhead==self.food:
                    self.eat()
                return list(newhead)
            else: #如果蛇撞牆或咬到自己
                self.gameover=True
        elif direction=='d' or direction=='D':
            newhead=(head[0]+1, head[1])
            if newhead in self.non_occupied:
                del self.non_occupied[newhead]
                if newhead==self.food:
                    self.eat()
                return list(newhead)
            else:
                self.gameover=True
        elif direction=='s' or direction=='S':
            newhead=(head[0], head[1]-1)
            if newhead in self.non_occupied:
                del self.non_occupied[newhead]
                if newhead==self.food:
                    self.eat()
                return list(newhead)
            else:
                self.gameover=True
        else:
            newhead=(head[0]-1, head[1])
            if newhead in self.non_occupied:
                del self.non_occupied[newhead]
                if newhead==self.food:
                    self.eat()
                return list(newhead)
            else:
                self.gameover=True

            
    #確認輸入的指令是否有效
    def validate(self, event):
        if self.direction=='w' or self.direction=='W':
            if event.char=='d' or event.char=='D':
                self.direction=event.char
            elif event.char=='a' or event.char=='A':
                self.direction=event.char
        elif self.direction=='d' or self.direction=='D':
            if event.char=='w' or event.char=='W':
                self.direction=event.char
            elif event.char=='s' or event.char=='S':
                self.direction=event.char
        elif self.direction=='s' or self.direction=='S':
            if event.char=='d' or event.char=='D':
                self.direction=event.char
            elif event.char=='a' or event.char=='A':
                self.direction=event.char
        else:
            if event.char=='w' or event.char=='W':
                self.direction=event.char
            elif event.char=='s' or event.char=='S':
                self.direction=event.char
    
    #蛇吃到食物時變長，再放一個新的食物
    def eat(self):
        self.occupied.append(self.oldbutt)
        self.food=random.choice(list(self.non_occupied))
        self.lbl_game_grid=tk.Label(master=self.frm_game_main, width=4, height=2, bg='white')
        self.lbl_game_grid.grid(row=(self.row-1-self.food[1]), column=self.food[0], padx=1, pady=1)
        self.score+=1
        self.score_var.set("   Your score: {}".format(self.score))
        self.lbl_score.update_idletasks()
        
if __name__=='__main__':
    game=tk.Tk()
    frm_main(game).grid(row=0, column=0)
    frm_main(game).startmenu()

    game.mainloop()


# In[ ]:





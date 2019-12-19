import solver
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class TestApp(App):
    def build(self):
        board=[[3,0,6,5,0,8,4,0,0], 
               [5,2,0,0,0,0,0,0,0], 
               [0,8,7,0,0,0,0,3,1], 
               [0,0,3,0,1,0,0,8,0], 
               [9,0,0,8,6,3,0,0,5], 
               [0,5,0,0,9,0,6,0,0], 
               [1,3,0,0,0,0,2,5,0], 
               [0,0,0,0,0,0,0,7,4], 
               [0,0,5,2,0,6,3,0,0]] 
        # solver.solve_board(board)
        layout = GridLayout(cols = 9, rows = 9)
        for row in board: 
            for num in row: 
                if num != 0: 
                    layout.add_widget(Button(text = str(num)))
                else: 
                    layout.add_widget(Button(text = ""))
        return layout
    

TestApp().run()

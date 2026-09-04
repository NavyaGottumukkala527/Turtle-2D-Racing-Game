import turtle
import random
import time

# Screen Setup
screen = turtle.Screen()
screen.title("Turtle Race")
screen.bgcolor("forestgreen")
screen.setup(width=900, height=700)
screen.tracer(0)

# Track Geometry and Turtle Setup
COLORS = ["red", "blue", "orange", "purple"]
START_X = -360
FINISH_X = 320
Y_POSITIONS = [120, 40, -40, -120]

def draw_track():
    drawer = turtle.Turtle()
    drawer.speed(0)
    drawer.hideturtle()
    drawer.penup()

    # Draw Track Area
    drawer.goto(-390, 180)
    drawer.color("gray20")
    drawer.begin_fill()
    for _ in range(2):
        drawer.forward(760)
        drawer.right(90)
        drawer.forward(340)
        drawer.right(90)
    drawer.end_fill()

    # Draw Finish Line
    drawer.goto(FINISH_X, 180)
    drawer.color("white")
    drawer.pensize(5)
    drawer.setheading(270)
    drawer.pendown()
    for _ in range(17):
        drawer.forward(10)
        drawer.penup()
        drawer.forward(10)
        drawer.pendown()

def create_turtles():
    turtles = []
    for i in range(4):
        t = turtle.Turtle(shape="turtle")
        t.color(COLORS[i])
        t.penup()
        t.shapesize(1.6)
        t.goto(START_X, Y_POSITIONS[i])
        turtles.append(t)
    return turtles

# Main Game loop
def main():
    player_data = {}  # {Player_Name: {"balance": 100, "streak": 0}}

    while True:
        screen.clearscreen()
        screen.bgcolor("forestgreen")
        screen.tracer(0)

        draw_track()
        turtles = create_turtles()
        screen.update()

        # 1. Prompt number of players
        num_players_input = screen.textinput("Setup", "How many players? (1-4):")
        if not num_players_input or not num_players_input.isdigit():
            num_players = 1
        else:
            num_players = min(max(int(num_players_input), 1), 4)

        # 2. Initialize players + collect bets
        current_bets = []
        for i in range(num_players):
            p_name = f"Player {i+1}"
            if p_name not in player_data:
                player_data[p_name] = {"balance": 100, "streak": 0}

            bal = player_data[p_name]["balance"]
            streak = player_data[p_name]["streak"]

            # Pick bet for turtle
            color_choice = screen.textinput(
                f"{p_name}'s Turn", 
                f"Bal: ${bal} | Streak: {streak}\nChoose turtle color ({', '.join(COLORS)}):"
            )
            if not color_choice or color_choice.lower() not in COLORS:
                color_choice = COLORS[i]
            else:
                color_choice = color_choice.lower()

            # Pick bet amount
            bet_input = screen.textinput(f"{p_name}'s Bet", f"Enter bet amount (Max ${bal}):")
            if bet_input and bet_input.isdigit():
                bet_amt = min(int(bet_input), bal)
            else:
                bet_amt = 10

            current_bets.append({
                "name": p_name,
                "color": color_choice,
                "amount": bet_amt
            })

        # 3. Run race
        winning_color = None
        racing = True
        while racing:
            time.sleep(0.03)
            for t in turtles:
                # Random movement speed per tick
                t.forward(random.randint(1, 12))
                if t.xcor() >= FINISH_X:
                    winning_color = t.pencolor()
                    racing = False
                    break
            screen.update()

        # 4. Resolve bets and update balances/winner
        results_msg = f"THE WINNER IS: {winning_color.upper()}!\n\n"
        for b in current_bets:
            p_name = b["name"]
            if b["color"] == winning_color:
                player_data[p_name]["balance"] += b["amount"]
                player_data[p_name]["streak"] += 1
                results_msg += f"• {p_name} WON ${b['amount']}! (Streak: {player_data[p_name]['streak']})\n"
            else:
                player_data[p_name]["balance"] -= b["amount"]
                player_data[p_name]["streak"] = 0
                results_msg += f"• {p_name} lost ${b['amount']}. (Streak Reset)\n"

        # 5. Show results and ask to replay
        replay = screen.textinput("Race Over!", results_msg + "\nPlay another round? (yes/no):")
        if not (replay and replay.lower().startswith("y")):
            break

    turtle.done()

if __name__ == "__main__":
    main()
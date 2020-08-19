Features:

- Validates all entered values by the player. This includes non numbers or invalid numbers or numbers for occupied spots.
- Computer takes between 1-3 seconds to make a move for added realism.
- Ability to keep playing after the game is finished.


Summary:

From my testing it seems that the fewest number of playouts to ensure the computer always wins or draws is roughly 30,000. When I had 
the value set to 20,000 I still had games where the computer would make a mistake or fall for a more complex set up. Once I bumped the 
value up to 30,000 I could no longer beat the computer even if I went first. The computer was even capable of doing more advanced moves 
and set up scenarios where it would surely win (It would have a possible win even after I blocked one move). At 30,000 playouts I was 
not able to win a game against the computer despite playing around 200 matches - it would always result in a draw.

For my move deciding algorithm I used a combination of priorities from the win/draw/loss random playouts.

An obvious win is always prioritized first, followed by preventing an obvious loss. If a move results in a win/loss prevention over 25% 
of the time, then that move must be the one made. If neither of these types of moves exist on the current board layout, then a move is 
chosen using a (win+loss)/draw ratio. In my testing I have found that if this ratio is less than 12.5 then a win/loss move is more significant
for the future versus playing for a draw. The lowest priority move is the one that results in a draw since it is the least significant option
usually, especially as the game progresses past the first few turns. The draw move algorithm is geared towards dealing with smarter players
early game and when the computer goes second (which is a disadvantage), while the win/loss algorithms are geared towards beating worse players
or ones who make mistakes.

I know it probably isn't very relevant but this one of the more interesting assignments I've had at SFU - simple but complex at the same time.
I had fun putting it together!

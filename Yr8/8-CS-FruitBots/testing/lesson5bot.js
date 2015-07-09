function new_game() {
}

function default_board_number(){
    return 1;
}

var visitedTarget = false;
var movingEast = true;

function moveToTarget(target_x,target_y){
    var my_x = get_my_x();
    var my_y = get_my_y();

    //Check to see if the target has been reached and set flag.
    if (my_x === target_x && my_y === target_y){
	visitedTarget = true;
    }
    else if (my_x < target_x){
	return EAST
    }
    else if (my_x > target_x){
	return WEST
    }
    else if (my_y < target_y){
	return SOUTH
    }
    else if (my_y > target_y){
	return NORTH
    }
}

function moveInSnake(){

    //Check if moving East and we're not at the edge of the board.
    if (movingEast === true && get_my_x() != WIDTH - 1){
	return EAST
    }
    //Check if moving West and not at the edge of the board.
    else if (movingEast === false && get_my_x() != 0){
	return WEST
    }
    //At edge so move South and then switch direction
    else if (get_my_x() === 0 || get_my_x() === WIDTH -1){
	movingEast = !movingEast;
	return SOUTH;
    }
}	 
    
function make_move(){
    board = get_board()

    //Check the flag to see if we've been to the target
    if (visitedTarget === false){
	return moveToTarget(0,0);
    }
    //Take the yummy fruit if it's there
    else if (board[get_my_x()][get_my_y()] > 0){
	return TAKE
    }
    //No fruit so let's move like a snake.
    else{
	return moveInSnake();
    }
}

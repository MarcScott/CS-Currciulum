function new_game() {
}

function default_board_number(){
    return 1;
}

visitedOrigin === false

function moveToOrigin(){
    my_x = get_my_x();
    my_y = get_my_y();
    if (my_x === 0 && my_y === 0){
	visitedOrigin = true;
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
    


function make_move(){
    if visitedOrigin === false{
	return moveToOrigin();
    }
}

function new_game() {
}

function default_board_number(){
    return 1;
}

//var target = [0,0]

function find_fruits(fruit){
    board = get_board();
    for(var i = 0; i < board.length; i++){
	for(var j = 0; j < board[i].length; j++){
	    if (board[i][j] === fruit){
		return [i,j]
	    }
	}
    }
}

function make_move(){
    target = find_fruits(4)
    my_x = get_my_x()
    my_y = get_my_y()
    target_x = target[0]
    target_y = target[1]
    
    if(my_x === target_x && my_y === target_y){
	return TAKE
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

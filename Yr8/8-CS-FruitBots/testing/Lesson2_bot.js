var target_x = 0;
var target_y = 0;

function new_game() {
}

function default_board_number(){
    return 1;
}

function make_move(){
    //get the board's 2d array
    board = get_board()

    //store the player's x and y position in variables for clearer code.
    var my_x = get_my_x()
    var my_y = get_my_y()
    console.log(get_board())
    
    if(board[my_x][my_y] > 0){
        return TAKE
    }

    else if(my_x < target_x){
        return EAST
    }
    else if(my_x > target_x){
        return WEST
    }
    else if(my_y < target_y){
        return SOUTH
    }
    else if(my_y > target_y){
        return NORTH
    }
    else{
        return PASS
    }
}

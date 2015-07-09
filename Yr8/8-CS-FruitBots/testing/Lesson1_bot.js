  var moving_east = false;

  function new_game() {
  }

  function make_move(){
      //log the board size and position
      console.log("The board's dimensions are " + WIDTH + " X " + HEIGHT);
      console.log("My FruitBot is at " + get_my_x() + "," + get_my_y());

      // detect if at the edge of the board
      if(get_my_x() === 0){
          moving_east = true;
      }
      if(get_my_x() === WIDTH-1){
          moving_east = false;
      }
      
      // move the bot
      if(moving_east === true){
          return EAST
      }
      else{
          return WEST
      }
  }

function playerMove() {
    if(firstChance===1){
        for(var i=0; i<4;i++){OldHands[i]=Hands[i];}
        firstChance=0;
    }
    updateScreen();
    var PrStatic=(Hands[3]===OldHands[3] && Hands[0]===OldHands[0]);
    var RtCrHt=((Hands[2]===(OldHands[2]+Hands[0])%5&&Hands[0]!==0)||(Hands[2]===(OldHands[2]+Hands[3])%5&&Hands[3]!==0));
    var LtCrHt=((Hands[1]===(OldHands[1]+Hands[0])%5&&Hands[0]!==0)||(Hands[1]===(OldHands[1]+Hands[3])%5&&Hands[3]!==0));
    var CrStatic=(Hands[2]===OldHands[2] && Hands[1]===OldHands[1]);
    var validPrSwitch=(((OldHands[0]+OldHands[3])===(Hands[0]+Hands[3]))&&OldHands[0]!==Hands[0]&&OldHands[3]!==Hands[3]&&Hands[0]!==OldHands[3]&&Hands[3]!==OldHands[0]&&Hands[0]<5&&Hands[3]<5);
    var notSuicide=true;
    if(((Hands[0]===0&&Hands[3]===5)||(Hands[3]===5&&Hands[0]===0)||(Hands[3]===0&&Hands[0]===0))){notSuicide=false;}

    if((PrStatic&&((Hands[1]===OldHands[1]&&RtCrHt&&OldHands[2]!==0)||(Hands[2]===OldHands[2]&&LtCrHt&&OldHands[1]!==0)))||(CrStatic&&validPrSwitch&&notSuicide)){validMove=1;}
    if(validMove===1){text("Type done to confirm your move and x to cancel it.",0.3625*width,0.62*height,190,300);}
    if(playerConfirmationStage===4){
        turn='computer';
        validMove=0;
        playerConfirmationStage=0;
        firstChance=1;
        if(train===5){
            playerStrat.push([OldHands[2],OldHands[3],OldHands[0],OldHands[1],Hands[2],Hands[3],Hands[0],Hands[1]]);
        }
    }
};

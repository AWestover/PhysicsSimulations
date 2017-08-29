function computerMove (){
    if(firstChance===1){
        for(var i=0; i<4;i++){OldHands[i]=Hands[i];}
        firstChance=0;
    }
    updateScreen();
    for(var z=0; z<Strat.length; z++){
        for(var p=0; p<4;p++){
            if(Strat[z][p]===OldHands[p]){
                Match+=1;
            }
        }
        if(Match===4){
            for(var k=0; k<4;k++){
                Hands[k]=Strat[z][k+4];
            }
            Strat.splice(z,1);
            Strat.push([OldHands[0],OldHands[1],OldHands[2],OldHands[3],Hands[0],Hands[1],Hands[2],Hands[3]]);
            validMove=1;
            break;
        }
        if(Match!==4){
            Match=0;
        }
    }
    while(validMove!==1){
        for(var i = 0; i<4; i++){Hands[i]=round(random(0,8));}
        var PrStatic=(Hands[3]===OldHands[3]&&Hands[0]===OldHands[0]);
        var RtPrHt=(((Hands[0]===(OldHands[0]+Hands[2])%5)&&Hands[2]!==0)||((Hands[0]===(OldHands[0]+Hands[1])%5)&&Hands[1]!==0));
        var LtPrHt=(((Hands[3]===(OldHands[3]+Hands[2])%5)&&Hands[2]!==0)||((Hands[3]===(OldHands[3]+Hands[1])%5)&&Hands[1]!==0));
        var CrStatic=(Hands[2]===OldHands[2]&&Hands[1]===OldHands[1]);
        var validCrSwitch=( ((OldHands[2]+OldHands[1]) === (Hands[2]+Hands[1])) && (OldHands[2]!==Hands[2]) && (OldHands[1]!==Hands[1]) && (Hands[1]!==OldHands[2]) && (Hands[2]!==OldHands[1]) && Hands[2]<5 && Hands[1]<5);
        var notSuicide=true;
        if(((Hands[1]===0&&Hands[2]===5)||(Hands[1]===5&&Hands[2]===0)||(Hands[1]===0&&Hands[2]===0))){
            notSuicide=false;
        }
        if(CrStatic&&Hands[3]===OldHands[3]&&RtPrHt&&OldHands[0]!==0){
            validMove=1;
        }
        if(CrStatic&&Hands[0]===OldHands[0]&&LtPrHt&&OldHands[3]!==0){
            if(validMove===1){
                validMove=2;
            }
            if(validMove===0){
                validMove=1;
            }
        }
        if(PrStatic&&validCrSwitch&&notSuicide&&Hands[2]!==OldHands[1]&&Hands[1]!==OldHands[2]){
            if(validMove!==0){
                validMove=0;
            }
            else if(validMove===0){
                validMove=1;
            }
        }
    }
    if(validMove===1){turn='player';firstChance=1;validMove=0;Match=0;}
};

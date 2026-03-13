import { Component, OnInit } from '@angular/core';
import { GameService } from '../../services/game.service';

@Component({
  selector: 'app-game',
  templateUrl: './game.component.html',
  styleUrls: ['./game.component.css']
})
export class GameComponent implements OnInit {
  players: any[] = [];
  gameState: any;

  constructor(private gameService: GameService) {}

  ngOnInit(): void {
    this.loadPlayers();
    this.initializeGame();
  }

  loadPlayers(): void {
    this.gameService.getPlayers().subscribe(data => {
      this.players = data;
    });
  }

  initializeGame(): void {
    this.gameService.startGame().subscribe(state => {
      this.gameState = state;
    });
  }

  makeMove(playerId: number, move: any): void {
    this.gameService.makeMove(playerId, move).subscribe(updatedState => {
      this.gameState = updatedState;
    });
  }

  startGame(): void {
    this.gameService.startGame().subscribe(state => {
      this.gameState = state;
    });
  }
}
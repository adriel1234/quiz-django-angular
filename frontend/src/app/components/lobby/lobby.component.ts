import { Component, OnInit } from '@angular/core';
import { GameService } from '../../services/game.service';

@Component({
  selector: 'app-lobby',
  templateUrl: './lobby.component.html',
  styleUrls: ['./lobby.component.css']
})
export class LobbyComponent implements OnInit {
  players: any[] = [];
  gameStarted: boolean = false;

  constructor(private gameService: GameService) {}

  ngOnInit(): void {
    this.loadPlayers();
  }

  loadPlayers(): void {
    this.gameService.getPlayers().subscribe((data: any[]) => {
      this.players = data;
    });
  }

  startGame(): void {
    this.gameService.startGame().subscribe(() => {
      this.gameStarted = true;
    });
  }
}
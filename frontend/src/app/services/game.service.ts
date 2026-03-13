import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { Player } from '../models/player.model';

@Injectable({
  providedIn: 'root'
})
export class GameService {
  private apiUrl = 'http://localhost:8000/api/games/';

  constructor(private http: HttpClient) { }

  getGames(): Observable<any> {
    return this.http.get(this.apiUrl);
  }

  getGameById(id: number): Observable<any> {
    return this.http.get(`${this.apiUrl}${id}/`);
  }

  createGame(gameData: any): Observable<any> {
    return this.http.post(this.apiUrl, gameData);
  }

  updateGame(id: number, gameData: any): Observable<any> {
    return this.http.put(`${this.apiUrl}${id}/`, gameData);
  }

  deleteGame(id: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}${id}/`);
  }

  getPlayersInGame(gameId: number): Observable<Player[]> {
    return this.http.get<Player[]>(`${this.apiUrl}${gameId}/players/`);
  }

  // Convenience methods used by components (stubs or simple proxies).
  getPlayers(): Observable<Player[]> {
    // If your backend exposes a players endpoint, change the URL below.
    try {
      return this.http.get<Player[]>('http://localhost:8000/api/players/');
    } catch (e) {
      return of([]);
    }
  }

  startGame(): Observable<any> {
    // Replace with real API call when available.
    return of({});
  }

  makeMove(playerId: number, move: any): Observable<any> {
    // Replace with real API call when available.
    return of({});
  }
}
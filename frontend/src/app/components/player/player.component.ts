import { Component, Input } from '@angular/core';
import { Player } from '../../models/player.model';

@Component({
  selector: 'app-player',
  templateUrl: './player.component.html',
  styleUrls: ['./player.component.css']
})
export class PlayerComponent {
  @Input() player!: Player;

  selectPlayer(): void {
    // Placeholder: can emit event or set selection state
    console.log('Player selected', this.player);
  }
}
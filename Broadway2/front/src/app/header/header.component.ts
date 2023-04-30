import {Component, EventEmitter, Output} from '@angular/core';
// import { LoginComponent} from "../login/login.component";
import { MatDialog} from "@angular/material/dialog";


@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent {
  constructor() {
  }
  @Output() sender = new EventEmitter();

  logout(value:boolean){
    this.sender.emit(value)
  }
 }

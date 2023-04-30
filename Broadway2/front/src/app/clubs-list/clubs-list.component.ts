import { Component } from '@angular/core';
import {ApiService} from "../api.service";
import {Club} from "../models";

@Component({
  selector: 'app-clubs-list',
  templateUrl: './clubs-list.component.html',
  styleUrls: ['./clubs-list.component.css']
})
export class ClubsListComponent {

  clubs_list: Club[] = [];

  constructor(private api: ApiService) {
    this.getAllClubs()
  }

  getAllClubs(){
    this.api.getClubList().subscribe((data) => {
      this.clubs_list = data
    })
  }


}

import { Component } from '@angular/core';
import { ApiService } from '../api.service';
import { Club } from '../models'

@Component({
  selector: 'app-clubs',
  templateUrl: './clubs.component.html',
  styleUrls: ['./clubs.component.css']
})
export class ClubsComponent {
  clubs_list: Club[] = [];
  constructor(private apiService: ApiService){}

  ngOnInit(){
    this.getMainClubs()
  }



  getMainClubs(){
    this.apiService.getMainClubs().subscribe((data) => {
      this.clubs_list = data;
    })
  }
}

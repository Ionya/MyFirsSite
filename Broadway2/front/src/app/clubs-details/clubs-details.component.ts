import { Component } from '@angular/core';
import { Club } from '../models';
import { ApiService } from '../api.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-clubs-details',
  templateUrl: './clubs-details.component.html',
  styleUrls: ['./clubs-details.component.css']
})
export class ClubsDetailsComponent {
  club: Club | undefined;

  constructor(private apiService: ApiService, private route: ActivatedRoute){}

  ngOnInit(){
    const routeParams = this.route.snapshot.paramMap;
    const clubIdFromRoute = Number(routeParams.get('id'));

    this.apiService.getClubElement(clubIdFromRoute).subscribe((data) => {
      this.club = data;
    })
  }

  deleteClub(){
    if(this.club){
      this.apiService.deleteClubElem(this.club.id).subscribe(response => {
        console.log(response);
      })
    }
  }

}

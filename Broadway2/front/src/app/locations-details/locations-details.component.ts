import { Component } from '@angular/core';
import { Location } from '../models';
import { ApiService } from '../api.service';
import { ActivatedRoute } from '@angular/router';
@Component({
  selector: 'app-locations-details',
  templateUrl: './locations-details.component.html',
  styleUrls: ['./locations-details.component.css']
})
export class LocationsDetailsComponent {
  location: Location | undefined;

  constructor(private apiService: ApiService, private route: ActivatedRoute){}

  ngOnInit(){
    const routeParams = this.route.snapshot.paramMap;
    const locationIdFromRoute = Number(routeParams.get('id'));

    this.apiService.getLocationElement(locationIdFromRoute).subscribe((data) => {
      this.location = data;
    })
  }

  deleteLocation(){
    if(this.location){
      this.apiService.deleteLocationElem(this.location.id).subscribe(response => {
        console.log(response);
      })
    }
  }
}

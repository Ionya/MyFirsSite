import { Component } from '@angular/core';
import { Location } from '../models';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-locations',
  templateUrl: './locations.component.html',
  styleUrls: ['./locations.component.css']
})
export class LocationsComponent {
  locations_list: Location[] = [];

  constructor(private apiService: ApiService){}

  ngOnInit(){
    this.getLocationsList();
  }

  getLocationsList(){
    return this.apiService.getLocationList().subscribe((data) => {
      this.locations_list = data;
    })
  }
}

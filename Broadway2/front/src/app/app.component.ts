import { Component } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Broadway2';
  logged: boolean = false;
  username: string = '';
  password: string = '';

  constructor(private apiService: ApiService){}

  ngOnInit(){
    const token = localStorage.getItem('token');
    if (token) {
      this.logged = true;
    }


  }

  login() {
    this.apiService.login(this.username, this.password).subscribe((data) => {
      localStorage.setItem('token', data.token);
      this.logged = true;
      this.username = '';
      this.password = '';
      // console.log(data)
    });
  }

  logout(value: boolean) {
    if(value == true){
      localStorage.removeItem('token');
      // Request to the Django
      this.logged = false;
    }
  }

  isLoggedIn(){
    return this.logged;
  }
}

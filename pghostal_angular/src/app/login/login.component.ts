import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {Router} from '@angular/router';
import {UserService} from '../user.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  loginForm!: FormGroup;

  constructor(
    private router: Router,
    private fb: FormBuilder,
    private userService: UserService
  ) {

    this.loginForm = this.fb.group({
      username: ['', Validators.required],
      password: ['', Validators.required]
    })

  }

  routeUser() {
    this.userService.getLogin(this.loginForm.value).subscribe((response: any) => {
      console.log(response, 'login response')
      if (response['isValid']) {
        this.router.navigate(['/user']);
      }

    }, error => {
      console.log(error, 'error')
      alert(error.error.message);
    })
  }

  ngOnInit() {

  }


}

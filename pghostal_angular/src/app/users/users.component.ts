import { Component, OnInit } from '@angular/core';
import { UserService } from '../user.service';
import { FormBuilder, FormGroup } from '@angular/forms';
import {Router} from "@angular/router";

@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.scss']
})
export class UsersComponent implements OnInit{

  users:any;
  allUsers:any
  searchTerm:any;
  userForm!:FormGroup;
  formTitle:string = '';

  constructor(
    private userService:UserService,
    private router:Router,
    private fb:FormBuilder)
  {


    this.userForm = this.fb.group({
      firstName: [''],
      lastName: [''],
      email: [''],
      parentName: [''],

      mobile: [''],
      module: [''],
      roomNumber: [''],
      blockName: [''],

      country:[''],
      studentId:['']

     })

  }

 

  logout():void{
    this.router.navigate(['/login']);
  }


  ngOnInit(){
    
  }


}

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

  addUserTitle(){
    this.formTitle='Add User';
  }

  editUserTitle(user:any){
    this.formTitle='Edit User';

    const data = {
      firstName: user.first_name,
      lastName: user.last_name,
      email: user.mail_id,
      parentName: user.parent_name,
      mobile: user.mobile,
      module: user.module,
      roomNumber: user.room_no,
      blockName: user.block_name,
      country: user.country,
      studentId: user.student_id
    }

    this.userForm.setValue(data)
  }

 
  clearForm(){
    this.userForm.reset()
  }

  deleteUser(user:any){
    this.userService.deleteUser(user.student_id).subscribe((response:any)=>{
      this.getAllUsers()
    })
  }
  getAllUsers(){
    this.userService.getUsers().subscribe((data:any)=>{
      this.users = data['results'];
      this.allUsers = data['results'];
    })
  } 

  searchUser(id:string){
    if(id){
      this.users = this.allUsers.filter((user:any)=>
        user.student_id.includes(id)
      )
    }
    else{
      this.users = this.allUsers;
    }
  }

  
  logout():void{
    this.router.navigate(['/login']);
  }




  ngOnInit(){
    this.getAllUsers()
  }


}

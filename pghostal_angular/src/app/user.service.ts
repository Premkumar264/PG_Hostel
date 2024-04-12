import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  baseUrl:string = 'http://127.0.0.1:5000'


  constructor(private http:HttpClient) { }

  getUsers(){
    return this.http.get(this.baseUrl + '/users')
  }

  getLogin(form:any){
    return this.http.post(this.baseUrl + '/login',form)
  }

  addUser(form:any){
    return this.http.post(this.baseUrl + '/users',form)

  }

  editUser(id:number,form:any){
    return this.http.put(this.baseUrl + '/user/'+ id , form)
  }

  deleteUser(id:number){
    return this.http.delete(this.baseUrl + '/users/'+ id)
  }

}

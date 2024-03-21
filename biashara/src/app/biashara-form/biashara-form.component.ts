import { CommonModule, NgIf } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import {MatRadioModule} from '@angular/material/radio'; 

@Component({
  selector: 'app-biashara-form',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule, NgIf, MatRadioModule],
  templateUrl: './biashara-form.component.html',
  styleUrl: './biashara-form.component.css'
})


export class BiasharaFormComponent implements OnInit { 
personalDetails!: FormGroup;
  addressDetails!: FormGroup;
  membershipDetails!: FormGroup;


  personal_step = false;
  address_step = false;
  membership_step = false;


  step = 1;

  constructor(private formBuilder: FormBuilder) {}

  ngOnInit() {
 
    this.personalDetails = this.formBuilder.group({
      name: ['', Validators.required],
      phone: ['', Validators.required],
      email: ['', Validators.required],
    });

    this.addressDetails = this.formBuilder.group({
      subCounty: ['', Validators.required],
      ward: ['', Validators.required],
      chama: ['', Validators.required],
      nameOfChama: ['', Validators.required],
 
    });

    this.membershipDetails = this.formBuilder.group({
      membershipPosition: ['', Validators.required],
      isChamaRegistered: ['Yes', Validators.required],
      chamaOperation: ['', Validators.required]
    });
  }



  get personal() {
    return this.personalDetails.controls;
  }

  get address() {
    return this.addressDetails.controls;
  }

  get membership() {
    return this.membershipDetails.controls;
  }
 



  next() {
    if (this.step == 1) {
      this.personal_step = true;
      if (this.personalDetails.invalid) {
        return;
      }
      this.step++;
    }
    if (this.step == 2) {
      this.address_step = true;
      if (this.addressDetails.invalid) {
        return;
      }
      this.step++;
    }
  }

  previous() {
    this.step--;
    if (this.step == 1) {
      this.personal_step = false;
    }
    if (this.step == 2) {
      this.membership_step = false;
    }
  }


  submit() {
    if (this.step == 3) {
      this.membership_step = true;
        console.log(this.personalDetails.value)
        console.log(this.addressDetails.value)
        console.log( this.membershipDetails.value);
        
      if (this.membershipDetails.invalid) {
        return;
      }
    }
  }

  














// ngOnInit(){
//   this.registerForm =new FormGroup({
//     firstName: new FormControl('', Validators.required),
//     lastName: new FormControl('', Validators.required),
//     phoneNumber: new FormControl('',[Validators.required, Validators.minLength(10)]),
//     emailAddress: new FormControl('', [Validators.required, Validators.email])
//   })


  
// }

// submitForm() {
//   console.warn(this.registerForm);
//   // console.log(this.registerForm.value);
//   }

   
}

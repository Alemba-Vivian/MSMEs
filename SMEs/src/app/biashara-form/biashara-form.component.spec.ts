import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BiasharaFormComponent } from './biashara-form.component';

describe('BiasharaFormComponent', () => {
  let component: BiasharaFormComponent;
  let fixture: ComponentFixture<BiasharaFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [BiasharaFormComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(BiasharaFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

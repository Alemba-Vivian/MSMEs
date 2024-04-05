import { TestBed } from '@angular/core/testing';

import { BiasharaServiceService } from './biashara-service.service';

describe('BiasharaServiceService', () => {
  let service: BiasharaServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(BiasharaServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});

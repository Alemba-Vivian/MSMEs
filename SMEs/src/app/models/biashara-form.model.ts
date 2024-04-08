// export class BiasharaForm {
//   name?: string;
//   phone?: number;
//   email?: string;
//   subCounty?: string;
//   ward?: string;
//   chama?: string;
//   nameOfChama?:string;
//   membershipPosition?: string;
//   isChamaRegistered?: boolean;
//   disability?: string;
//   chamaOperation?:string;
// }


export class BiasharaForm {
  personalDetails: {
    name?: string;
    phone?: string;
    email?: string;
    disability?: boolean;
  }= {};
  addressDetails: {
    subCounty?:string;
    ward?: string;
    chama?: string;
    nameOfChama?: string;
  }= {};
  membershipDetails: {
    membershipPosition?: string;
    isChamaRegistered?: boolean;
    chamaOperation?: string;
  }= {};
}

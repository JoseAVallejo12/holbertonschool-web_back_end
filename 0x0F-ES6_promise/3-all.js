import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  let data = {};
  uploadPhoto()
    .then(({ body }) => { data += body })
    .then(() => createUser({
      ...
    }));

}

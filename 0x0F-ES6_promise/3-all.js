import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  uploadPhoto()
    .then(({ body }) => body)
    .then((body) => createUser().then(({ firstName, lastName }) => console.log(`${body} ${firstName} ${lastName}`)));
}

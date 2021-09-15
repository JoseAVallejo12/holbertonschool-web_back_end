import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ])
    .then((values) => values.map((data) => {
      if (data.reason) {
        return {
          status: data.status,
          value: data.reason.message,
        };
      }
      return {
        status: data.status,
        value: `${data.value.firstName} ${data.value.lastName}`,
      };
    }));
}

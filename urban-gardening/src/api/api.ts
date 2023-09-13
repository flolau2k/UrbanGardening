export const fetchData = (apiUrl: string): any => {
  fetch(apiUrl, {
    method: 'GET',
    headers: {
      Authorization: 'Bearer ACCESS_TOKEN',
      'Content-Type': 'application/json'
    }
  })
    .then((response: any) => response.json())
    .then((data: any) => {
      // Handle data
      console.log(data)
      return data
    })
    .catch((error) => {
      // Handle the error
      console.error('There was a problem with the fetch:', error)
      throw new Error(error.message)
    })
}

export const postData = (apiUrl: string, payload: any): any => {
  fetch(apiUrl, {
    method: 'POST',
    headers: {
      Authorization: 'Bearer ACCESS_TOKEN',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload)
  })
    .then((response: any) => response.json())
    .then((data: any) => {
      // Handle response
      console.log(data)
    })
    .catch((error) => {
      // Handle the error
      console.error('There was a problem with the post:', error)
      throw new Error(error.message)
    })
}

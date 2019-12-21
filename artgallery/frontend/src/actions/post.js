import axios from "axios";

import { GET_POST } from "./types";

export const getPost = () => dispatch => {
  axios
    .get("./api/post/")
    .then(res => {
      dispatch({
        type: GET_POST,
        payload: res.data
      });
    })
    .catch(err =>
      dispatch(returnErrors(err.response.data, err.response.status))
    );
};

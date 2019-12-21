import React, { Component } from "react";
import { connect } from "react-redux";
import PropTypes from "prop-types";
import { getPost } from "../../actions/post";

export class Post extends Component {
  static propTypes = {
    post: PropTypes.array.isRequired
  };

  componentDidMount() {
    this.props.getPost();
  }

  render() {
    return (
      <div>
        <div>
          <img src="https://placekitten.com/g/200/200" />
          <img src="https://placekitten.com/g/200/200" />
        </div>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  post: state.post.post
});

export default connect(mapStateToProps, { getPost })(Post);

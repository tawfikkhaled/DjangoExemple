import { Interface } from "node:readline";
import React, { Component, MouseEventHandler } from "react";
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Form,
  FormGroup,
  Input,
  Label,
} from "reactstrap";

  
  export class IStateModel {
    file
  }
  
  export interface IPropsModel {
    toggle : MouseEventHandler<any>
    onSave : any
}

export default class CustomModalUpload extends Component<IPropsModel, IStateModel> {
  constructor(props) {
    super(props);
    this.state = {
      file : ""
    };
  }

  handleChange = (e) => {
    let { name, value } = e.target;
    if (e.target.files != undefined && e.target.files.length>0)
      this.setState({file : e.target.files[0]})
    if (e.target.type === "checkbox") {
      value = e.target.checked;
    }
  };

  render() {
    const { toggle, onSave } = this.props;

    return (
      <Modal isOpen={true} toggle={toggle}>
        <ModalHeader toggle={toggle}>Uploading File</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="todo-title">Upload File</Label>
              <Input
                type="file"
                id="file-upload"
                name="file-upload-title"
                //value={this.state.activeItem.title}
                onChange={this.handleChange}
                placeholder="choose file"
              />
            </FormGroup>
            <FormGroup>
              <Label for="defaultVaLues">Description</Label>
              <Input
                type="text"
                id="defaultVaLues"
                name="defaultvalues"
                value=""
                onChange={this.handleChange}
                placeholder="enter default values"
              />
            </FormGroup>
          </Form>
        </ModalBody>
        <ModalFooter>
          <Button
            color="success"
            onClick={() => onSave(this.state.file)}
          >
            Save
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}